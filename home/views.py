from django.shortcuts import render, redirect
from .models import Donor,Organ,Looking,Subscribe, State, City
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse 
from django.views import View
from captcha.fields import ReCaptchaField


class CaptchaChallengeView(View):
    template_name = 'captcha_page.html'

    def get(self, request):
        form = ReCaptchaField()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ReCaptchaField(request.POST)
        if form:
            return redirect('home:index')
        else:
            pass

        return render(request, self.template_name, {'form': form})

               
def index(request):
    if request.method == "POST":
           if request.POST.get("form_type")=='subscribe':
            from_email = request.POST.get("email")
            send_mail(
            subject=f"Welcome to SANJIVANI!!",
            message=f"Dear Subscriber,\n\n"
        f"Thank you for subscribing to SANJIVANI! We are honored to have you join our community. Stay updated with life-saving news, events, and breakthroughs at SANJIVANI. Expect exclusive content and valuable insights delivered straight to your inbox.\n\n"
        f"Your voice matters! Feel free to share your feedback, suggestions, or any questions you may have. Together, we can make a difference and save lives.\n\n"
        f"Best regards,\n"
        f"The SANJIVANI Team",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[from_email],
        )
            subscriber = Subscribe(email=from_email)
            subscriber.save()
            messages.success(request, "Thanks For Subscribing.",extra_tags="subscribe")
    return render(request,"index.html")


def events(request):
    if request.method == "POST":
          if request.POST.get("form_type")=='subscribe':
            from_email = request.POST.get("email")
            send_mail(
            subject=f"Welcome to SANJIVANI!!",
            message=f"Dear Subscriber,\n\n"
        f"Thank you for subscribing to SANJIVANI! We are honored to have you join our community. Stay updated with life-saving news, events, and breakthroughs at SANJIVANI. Expect exclusive content and valuable insights delivered straight to your inbox.\n\n"
        f"Your voice matters! Feel free to share your feedback, suggestions, or any questions you may have. Together, we can make a difference and save lives.\n\n"
        f"Best regards,\n"
        f"The SANJIVANI Team",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[from_email],
        )
            subscriber = Subscribe(email=from_email)
            subscriber.save()
            messages.success(request, "Thanks For Subscribing!!",extra_tags="subscribe")
    return render(request,"events.html")


def check(request):
    is_eligible = None
    reason = None
    name = None
    if request.method == 'POST':
        name = request.POST.get('name')
        age = int(request.POST.get('age'))
        weight = float(request.POST.get('weight'))
        hemoglobin = float(request.POST.get('hemoglobin'))
        pregnant = request.POST.get('pregnant')
        tattoos = request.POST.get('tattoos')
        medical_history = request.POST.get('medical_history')
        recent_blood_transfusion=request.POST.get('recent_blood_transfusion')
        donate = request.POST.get('donate')
        # Perform your eligibility checks here
        error_messages = []

        if age < 18 or age > 65:
            error_messages.append("You must be between 18 and 65 years old to donate blood.")
        
        if weight < 50:
            error_messages.append("You must weigh at least 50 kg to donate blood.")
        
        if hemoglobin < 12:
            error_messages.append("Your hemoglobin level must be at least 12.5 g/dL to donate blood.")
        
        if pregnant == 'Yes':
            error_messages.append("Pregnant individuals are not eligible to donate blood.")
        
        if tattoos == 'Yes':
            error_messages.append("Individuals with tattoos or piercings in the last 12 months are not eligible to donate blood.")
        
        if medical_history in ['HIV', 'Diabetes', 'Hepatitis', 'Cancer']:
            error_messages.append("Individuals with such medical history are not eligible to donate blood.")
        
        if recent_blood_transfusion == 'Yes':
            error_messages.append("Recent blood transfusions may affect your eligibility to donate blood.")

        if donate == 'Yes':
            error_messages.append("You are not eligible to donate blood if you have donated in the last 3 months.")

        if error_messages:
            is_eligible = False
            reason = ', '.join(error_messages)
        else:
            is_eligible = True

        return render(request, 'check.html', {'is_eligible': is_eligible, 'reason': reason, 'name': name})

    if request.method == "POST":
           if request.POST.get("form_type")=='subscribe':
            from_email = request.POST.get("email")
            send_mail(
            subject=f"Welcome to SANJIVANI!!",
            message=f"Dear Subscriber,\n\n"
        f"Thank you for subscribing to SANJIVANI! We are honored to have you join our community. Stay updated with life-saving news, events, and breakthroughs at SANJIVANI. Expect exclusive content and valuable insights delivered straight to your inbox.\n\n"
        f"Your voice matters! Feel free to share your feedback, suggestions, or any questions you may have. Together, we can make a difference and save lives.\n\n"
        f"Best regards,\n"
        f"The SANJIVANI Team",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[from_email],
        )
            subscriber = Subscribe(email=from_email)
            subscriber.save()
            messages.success(request, "Thanks For Subscribing.",extra_tags="subscribe")
    return render(request,"check.html")


def join(request):
    if request.method == "POST":
           if request.POST.get("form_type")=='subscribe':
            from_email = request.POST.get("email")
            send_mail(
            subject=f"Welcome to SANJIVANI!!",
            message=f"Dear Subscriber,\n\n"
        f"Thank you for subscribing to SANJIVANI! We are honored to have you join our community. Stay updated with life-saving news, events, and breakthroughs at SANJIVANI. Expect exclusive content and valuable insights delivered straight to your inbox.\n\n"
        f"Your voice matters! Feel free to share your feedback, suggestions, or any questions you may have. Together, we can make a difference and save lives.\n\n"
        f"Best regards,\n"
        f"The SANJIVANI Team",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[from_email],
        )
            subscriber = Subscribe(email=from_email)
            subscriber.save()
            messages.success(request, "Thanks For Subscribing.",extra_tags="subscribe")
    return render(request,"join.html")


def faq(request):
    if request.method == "POST":
           if request.POST.get("form_type")=='subscribe':
            from_email = request.POST.get("email")
            send_mail(
            subject=f"Welcome to SANJIVANI!!",
            message=f"Dear Subscriber,\n\n"
        f"Thank you for subscribing to SANJIVANI! We are honored to have you join our community. Stay updated with life-saving news, events, and breakthroughs at SANJIVANI. Expect exclusive content and valuable insights delivered straight to your inbox.\n\n"
        f"Your voice matters! Feel free to share your feedback, suggestions, or any questions you may have. Together, we can make a difference and save lives.\n\n"
        f"Best regards,\n"
        f"The SANJIVANI Team",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[from_email],
        )
            subscriber = Subscribe(email=from_email)
            subscriber.save()
            messages.success(request, "Thanks For Subscribing.",extra_tags="subscribe")
    return render(request,"faq.html")


def contact(request):
    if request.method == "POST":
             if request.POST.get("form_type")=='contact':
                name=request.POST.get("name")
                from_email = request.POST.get("email")
                phone= request.POST.get('phone')
                message = request.POST.get("message") 
                recipient_list = [settings.EMAIL_HOST_USER]
                send_mail(
                subject=f"Feedback from {name}",
                message=f"name: {name}\n\nphone: {phone}\n\nmessage: {message}\n\nemail:{from_email}",
                from_email=from_email,
                recipient_list=recipient_list,
            )
                messages.success(request, "Thanks Cutie",extra_tags="contact")
                return redirect('home:contact')
    if request.POST.get("form_type")=='subscribe':
            from_email = request.POST.get("email")
            send_mail(
            subject=f"Welcome to SANJIVANI!!",
            message=f"Dear Subscriber,\n\n"
        f"Thank you for subscribing to SANJIVANI! We are honored to have you join our community. Stay updated with life-saving news, events, and breakthroughs at SANJIVANI. Expect exclusive content and valuable insights delivered straight to your inbox.\n\n"
        f"Your voice matters! Feel free to share your feedback, suggestions, or any questions you may have. Together, we can make a difference and save lives.\n\n"
        f"Best regards,\n"
        f"The SANJIVANI Team",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[from_email],
            )
            subscriber = Subscribe(email=from_email)
            subscriber.save()
            messages.success(request, "Thanks For Subscribing.",extra_tags="subscribe")
    return render(request,"contact.html")

def get_cities(request):
    state_name = request.GET.get('state_name')
    cities = City.objects.filter(state__name=state_name)
    data = [{'id': city.id, 'name': city.name} for city in cities]
    return JsonResponse(data, safe=False)
    
# Donor Blood
def donor(request):
    states=State.objects.all()
    cities=City.objects.none()

    if request.method == 'POST': 
        if request.POST.get("form_type")=='donor':
            name = request.POST.get("name")
            mail = request.POST.get("mail")
            phone = request.POST.get("phone")
            dob = request.POST.get("dob")
            gender = request.POST.get("gender")
            address = request.POST.get("address")
            history = request.POST.get("history")
            blood = request.POST.get("blood_group")
            state=request.POST.get("state")
            cities = City.objects.filter(name=request.GET.get('state'))
            cities_v = request.POST.get('city')
            
        # Create the Donor object and save it to the database
            donor= Donor(
                name=name,
                email=mail,
                phone=phone,
                dob=dob,
                gender=gender,
                address=address,
                state=state,
                city=cities_v,
                med_history=history,
                blood=blood
            )
            donor.save()
            messages.success(request, "Donor information saved successfully.",extra_tags="donor")
            return redirect('home:donor')
        
        if request.POST.get("form_type")=='subscribe':
            from_email = request.POST.get("email")
            send_mail(
            subject=f"Welcome to SANJIVANI!!",
            message=f"Dear Subscriber,\n\n"
        f"Thank you for subscribing to SANJIVANI! We are honored to have you join our community. Stay updated with life-saving news, events, and breakthroughs at SANJIVANI. Expect exclusive content and valuable insights delivered straight to your inbox.\n\n"
        f"Your voice matters! Feel free to share your feedback, suggestions, or any questions you may have. Together, we can make a difference and save lives.\n\n"
        f"Best regards,\n"
        f"The SANJIVANI Team",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[from_email],
        )
            subscriber = Subscribe(email=from_email)
            subscriber.save()
            messages.success(request, "Thanks For Subscribing.",extra_tags="subscribe")

    return render(request, "donor.html", {'states': states, 'cities': cities})



# Donor Organ
def organ(request):
    states=State.objects.all()
    cities=City.objects.none()
    if request.method == 'POST':
        if request.POST.get("form_type")=='organ':
            name = request.POST.get("name")
            mail = request.POST.get("mail")
            phone = request.POST.get("phone")
            dob = request.POST.get("dob")
            gender = request.POST.get("gender")
            address = request.POST.get("address")
            donate = request.POST.getlist("donate")
            other = request.POST.get("other")
            donate_tissue = request.POST.getlist("donate_tissue")
            proof = request.POST.get("proof")
            donate_list=','.join(donate)
            donate_tissue_list=','.join(donate_tissue)
            state=request.POST.get("state")
            cities = City.objects.filter(name=request.GET.get('state'))
            cities_v = request.POST.get('city')

            organ= Organ(
                name=name,
                email=mail,
                phone=phone,
                dob=dob,
                gender=gender,
                address=address,
                state=state,
                city=cities_v,
                donate=donate_list,
                other=other,
                donate_tissue=donate_tissue_list,
                proof=proof
            )
            organ.save()
            messages.success(request, "Donor information saved successfully.",extra_tags="organ")
            return redirect('home:organ')
        
        if request.POST.get("form_type")=='subscribe':
                from_email = request.POST.get("email")
                send_mail(
                subject=f"Welcome to SANJIVANI!!",
                message=f"Dear Subscriber,\n\n"
            f"Thank you for subscribing to SANJIVANI! We are honored to have you join our community. Stay updated with life-saving news, events, and breakthroughs at SANJIVANI. Expect exclusive content and valuable insights delivered straight to your inbox.\n\n"
            f"Your voice matters! Feel free to share your feedback, suggestions, or any questions you may have. Together, we can make a difference and save lives.\n\n"
            f"Best regards,\n"
            f"The SANJIVANI Team",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[from_email],
            )
                subscriber = Subscribe(email=from_email)
                subscriber.save()
                messages.success(request, "Thanks For Subscribing.",extra_tags="subscribe")
    
    return render(request,"organ.html", {'states': states, 'cities': cities})


# Looking
def looking(request):
    states=State.objects.all()
    cities=City.objects.none()
    if request.method == 'POST':
        if request.POST.get("form_type")=='looking':
            name = request.POST.get("name")
            patient = request.POST.get("patient")
            mail = request.POST.get("mail")
            phone = request.POST.get("phone")
            dob = request.POST.get("dob")
            address = request.POST.get("address")
            units = request.POST.get("units")
            blood = request.POST.get("blood_group")
            require = request.POST.get("require")
            state=request.POST.get("state")
            cities = City.objects.filter(name=request.GET.get('state'))
            cities_v = request.POST.get('city')

            looking= Looking(
                name=name,
                patient=patient,
                email=mail,
                phone=phone,
                dob=dob,
                address=address,
                state=state,
                city=cities_v,
                units=units,
                blood=blood,
                require=require
            )
            looking.save()
            return redirect('home:display_donor', donor_id=looking.blood)
        
        if request.POST.get("form_type")=='subscribe':
                from_email = request.POST.get("email")
                send_mail(
                subject=f"Welcome to SANJIVANI!!",
                message=f"Dear Subscriber,\n\n"
            f"Thank you for subscribing to SANJIVANI! We are honored to have you join our community. Stay updated with life-saving news, events, and breakthroughs at SANJIVANI. Expect exclusive content and valuable insights delivered straight to your inbox.\n\n"
            f"Your voice matters! Feel free to share your feedback, suggestions, or any questions you may have. Together, we can make a difference and save lives.\n\n"
            f"Best regards,\n"
            f"The SANJIVANI Team",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[from_email],
            )
                subscriber = Subscribe(email=from_email)
                subscriber.save()
                messages.success(request, "Thanks For Subscribing.",extra_tags="subscribe")

    return render(request,"looking.html", {'states': states, 'cities': cities})

def display_donor(request, donor_id):
    donor = Donor.objects.filter(blood=donor_id)
    context = {
        'donor': donor
    }
    return render(request, "redirect.html", context)
