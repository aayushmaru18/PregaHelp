from calendar import calendar
from django.shortcuts import render,redirect
from django.conf import settings
from due_date_calculator import Calculate_EDD
import datetime
from blogs import Blogs
from web_scrape_doctor import Consulate
import joblib
from dateutil.relativedelta import relativedelta
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

# Create your views here.

def index(request):
    return render(request,'index.html')

def blogs(request):

    if request.method == 'POST':
        category = request.POST['flexRadioDefault']

        if category == 'Food':
            content = Blogs.Food()
            blog_name = 'Food'

        else:
            content = Blogs.Health()
            blog_name = 'Health'

        return render(request,'blogs.html', {"content": content, 'blog_name': blog_name})

    content = Blogs.Food()
    blog_name = 'Food'

    return render(request,'blogs.html', {"content": content, 'blog_name': blog_name})

def due_date_calculator(request):

    x = [i for i in range(20, 46, 1)]

    if request.method == 'POST':
        
        if request.POST['duedate'] == "menstrual":
            date = request.POST['men_date']
            average_cycle_length = request.POST['cyclelength']
            print(request.POST['duedate'], date, average_cycle_length)

            yr, mon, day = date.split("-")
            last_menstrual_period = datetime.date(int(yr), int(mon), int(day))

            EDD = Calculate_EDD(last_menstrual_period, int(average_cycle_length))

            dd_yr, dd_mon, dd_day = str(EDD.calculate()).split("-")
            
            mon = EDD.calculate().strftime("%B")

            due_date_st = f"{mon} {dd_day}, {dd_yr} {EDD.calculate().strftime('%A')}"
            
            return render (request,'due-date-calculator.html', {"EDD": due_date_st})

        else:
            date = request.POST['ovul_date']

            yr, mon, day = date.split("-")
            last_menstrual_period = datetime.date(int(yr), int(mon), int(day))

            due_date = last_menstrual_period + relativedelta(days=266)

            dd_yr, dd_mon, dd_day = str(due_date).split("-")
            
            mon = due_date.strftime("%B")

            due_date_st = f"{mon} {dd_day}, {dd_yr} {due_date.strftime('%A')}"

            return render (request,'due-date-calculator.html', {"EDD": due_date_st})

    return render (request,'due-date-calculator.html', {"option_loop": x})

def consultation(request):

    if request.method == 'POST':
        city_name = request.POST['query']

        dr_list = Consulate(city_name.capitalize()).get_doctors()
        
        return render(request,'consultation.html', {"dr_list": dr_list})
        
    return render(request,'consultation.html')

def baby_weight(request):
    if request.method == 'POST':
        
        FAGE = request.POST['fatherage']
        GAINED = request.POST['weight']
        VISITS = request.POST['prenatal']
        MAGE = request.POST['mother']
        WEEKS = request.POST['gestional']
        RACEMOM = request.POST['RACEMOM']
        RACEDAD = request.POST['RACEDAD']
        CIGNUM = request.POST['Cignum']
        DRINKNUM = request.POST['drink']
        DIABETES = request.POST['diabetes']
        HYPERPR = request.POST['Hypertension']
        CERVIX = request.POST['cervix']
        PRETERM = request.POST['preterm']
        anemia = request.POST['Anemia']

        test_data = [[FAGE, GAINED, VISITS, MAGE, WEEKS, int(RACEMOM), int(RACEDAD), 
        CIGNUM, DRINKNUM, int(anemia), int(DIABETES), int(HYPERPR), int(CERVIX), int(PRETERM)]]
        
        #print(test_data)

        model = joblib.load("finalized_model_BW.sav")
        predicted = model.predict(test_data)
        
        return render(request,'baby-weight.html', {"predicted": round(predicted[0], 2)})

    return render(request,'baby-weight.html')

def maternal_health_risk(request):

    if request.method == 'POST':
        age = request.POST['mother']
        sbp = request.POST['sbp']
        dbp = request.POST['dsbp']
        bsl = request.POST['bgl']
        temp = request.POST['bt']
        heart_rate = request.POST['hr']

        model = joblib.load("finalized_model_RFR.sav")
        predicted = model.predict([[age, sbp, dbp, bsl, temp, heart_rate]])
        #print(predicted)

        risk = None

        if (predicted[0] >= 1.5) and (predicted[0] <= 2.5):
            risk = "Medium"

        elif (predicted[0] >= 0) and (predicted[0] < 1.5):
            risk = "Low"

        else:
            risk = "High"

        #print(risk)
        return render(request,'maternal-health.html', {'risk': risk})
            

    return render(request,'maternal-health.html')

def calendar(request):
    return render(request,'calendar.html')

def week_one(request):
    return render(request,'week_one.html')

def book_appoitnment(request, dr_name, hospital_name):

    #print(dr_name, hospital_name)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        address = request.POST['address']
        ambu_q = request.POST['ambulance']

        msg_html = render_to_string('mailing.html', {"dr_name": dr_name, "hospital_name": hospital_name, "name": name})

        email = EmailMultiAlternatives(f'PregaHelp - Appointment Scheduling', '', settings.EMAIL_HOST_USER, [email])
        email.attach_alternative(msg_html, "text/html")
        email.send()

        return redirect('index')

    return render(request,'book-appoitnment.html', {"dr_name": dr_name, "hospital_name": hospital_name})
