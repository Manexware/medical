from openerp import models,fields

class DrugsRecreational(models.Model):
    
    _name = 'oemedical.drugs_recreational'
    _description = 'Recreational Drug'


    name = fields.Char('Name', translate=True, help="Name of the drug")
    street_name = fields.Char('Street names',
        help="Common name of the drug in street jargon")

    toxicity = fields.Selection([
        ('0', 'None'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Extreme'),
        ], 'Toxicity', sort=False)

    addiction_level = fields.Selection([
        ('0', 'None'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Extreme'),
        ], 'Dependence', sort=False)

    legal_status = fields.Selection([
        ('0', 'Legal'),
        ('1', 'Illegal'),
        ], 'Legal Status', sort=False)

    category = fields.Selection([
        ('cannabinoid', 'Cannabinoids'),
        ('depressant', 'Depressants'),
        ('dissociative', 'Dissociative Anesthetics'),
        ('hallucinogen', 'Hallucinogens'),
        ('opioid', 'Opioids'),
        ('stimulant', 'Stimulants'),
        ('other', 'Others'),
        ], 'Category', sort=False)

    withdrawal_level = fields.Integer('Withdrawal',
        help="Presence and severity of characteristic withdrawal "
        "symptoms.\nUsing Henningfield rating. 1=highest and 6=lowest")

    reinforcement_level = fields.Integer('Reinforcement',
        help="A measure of the substance's ability to get users to take it "
        " again and again, and in preference to other substances.\nUsing "
        " Henningfield rating. 1=highest and 6=lowest")

    tolerance_level = fields.Integer('Tolerance',
        help="How much of the substance is needed to satisfy increasing "
        "cravings for it, and the level of stable need that is eventually "
        "reached.\nUsing Henningfield rating. 1=highest and 6=lowest")

    dependence_level = fields.Integer('Dependence',
        help="How difficult it is for the user to quit, the relapse rate, "
        "the percentage of people who eventually become dependent, the "
        "rating users give their own need for the substance and the "
        "degree to which the substance will be used in the face of "
        "evidence that it causes harm.\nUsing Henningfield rating. "
        "1=highest and 6=lowest")

    intoxication_level = fields.Integer('Intoxication',
        help="the level of intoxication is associated with addiction and "
        "increases the personal and social damage a substance may do. \n"
        "Using Henningfield rating. 1=highest and 6=lowest")

    route_oral = fields.Boolean('Oral')

    route_popping = fields.Boolean('Skin Popping',
        help="Subcutaneous or Intradermical administration")

    route_inhaling = fields.Boolean('Smoke / Inhale',
        help="Insufflation, excluding nasal")

    route_sniffing = fields.Boolean('Sniffing',
        help="Also called snorting - inhaling through the nares  ")

    route_injection = fields.Boolean('Injection',
        help="Injection - Intravenous, Intramuscular...")

    dea_schedule_i = fields.Boolean('DEA schedule I',
        help="Schedule I and II drugs have a high potential for abuse. "
        "They require greater storage security and have a quota on "
        "manufacturing, among other restrictions. Schedule I drugs are "
        "available for research only and have no approved medical use; "
        "Schedule II drugs are available only by prescription "
        "(unrefillable) and require a form for ordering. Schedule III "
        "and IV drugs are available by prescription, may have five "
        "refills in 6 months, and may be ordered orally. "
        "Some Schedule V drugs are available over the counter")

    dea_schedule_ii = fields.Boolean('II',
        help="Schedule I and II drugs have a high potential for abuse."
        "They require greater storage security and have a quota on"
        "manufacturing, among other restrictions. Schedule I drugs are"
        "available for research only and have no approved medical use; "
        "Schedule II drugs are available only by prescription "
        "(unrefillable) and require a form for ordering. Schedule III "
        "and IV drugs are available by prescription, may have five"
        "refills in 6 months, and may be ordered orally. "
        "Some Schedule V drugs are available over the counter")

    dea_schedule_iii = fields.Boolean('III',
        help="Schedule I and II drugs have a high potential for abuse. "
        "They require greater storage security and have a quota on "
        "manufacturing, among other restrictions. Schedule I drugs are "
        "available for research only and have no approved medical use; "
        "Schedule II drugs are available only by prescription "
        "(unrefillable) and require a form for ordering. Schedule III "
        "and IV drugs are available by prescription, may have five "
        "refills in 6 months, and may be ordered orally. "
        "Some Schedule V drugs are available over the counter")

    dea_schedule_iv = fields.Boolean('IV',
        help="Schedule I and II drugs have a high potential for abuse. "
        "They require greater storage security and have a quota on "
        "manufacturing, among other restrictions. Schedule I drugs are "
        "available for research only and have no approved medical use; "
        "Schedule II drugs are available only by prescription "
        "(unrefillable) and require a form for ordering. Schedule III "
        "and IV drugs are available by prescription, may have five "
        "refills in 6 months, and may be ordered orally. "
        "Some Schedule V drugs are available over the counter")

    dea_schedule_v = fields.Boolean('V',
        help="Schedule I and II drugs have a high potential for abuse. "
        "They require greater storage security and have a quota on "
        "manufacturing, among other restrictions. Schedule I drugs are "
        "available for research only and have no approved medical use; "
        "Schedule II drugs are available only by prescription "
        "(unrefillable) and require a form for ordering. Schedule III "
        "and IV drugs are available by prescription, may have five "
        "refills in 6 months, and may be ordered orally. "
        "Some Schedule V drugs are available over the counter")

    info = fields.Text('Extra Info')



class PatientRecreationalDrugs(models.Model):
    
    _name = 'oemedical.patient.recreational_drugs'
    _description = 'Patient use of Recreational Drugs'

    patient_id = fields.Many2one('oemedical.patient', 'Patient')
    recreational_drug = fields.Many2one('oemedical.drugs_recreational', 'Recreational Drug')

''' CAGE questionnaire to assess patient dependency to alcohol '''

class PatientCAGE(models.Model):

    _name = 'oemedical.patient.cage'
    _description =  'Patient CAGE Questionnaire'

    name = fields.Many2one('oemedical.patient', 'Patient', required=True)
    evaluation_date = fields.Datetime('Date')
    cage_c = fields.Boolean('Hard to Cut down', help='Have you ever felt you needed to Cut down on your drinking ?')
    cage_a = fields.Boolean('Angry with Critics', help='Have people Annoyed you by criticizing your drinking ?')
    cage_g = fields.Boolean('Guilt', help='Have you ever felt Guilty about drinking ?')
    cage_e = fields.Boolean('Eye-opener', help='Have you ever felt you needed a drink first thing in the morning (Eye-opener) to steady your nerves or to get rid of a hangover?')
    cage_score = fields.Integer('CAGE Score')

class MedicalPatient(models.Model):

    _inherit='oemedical.patient'


    exercise = fields.Boolean('Exercise')
    exercise_minutes_day = fields.Integer('Minutes / day', help="How many minutes a day the patient exercises")
    sleep_hours = fields.Integer('Hours of sleep', help="Average hours of sleep per day")
    sleep_during_daytime = fields.Boolean('Sleeps at daytime', help="Check if the patient sleep hours are during daylight rather than at night")
    number_of_meals = fields.Integer('Meals per day')
    eats_alone = fields.Boolean('Eats alone', help="Check this box if the patient eats by him / herself.")
    salt = fields.Boolean('Salt',  help="Check if patient consumes salt with the food")
    coffee = fields.Boolean('Coffee')
    coffee_cups = fields.Integer('Cups per day', help="Number of cup of coffee a day")
    soft_drinks = fields.Boolean('Soft drinks (sugar)', help="Check if the patient consumes soft drinks with sugar")
    diet = fields.Boolean('Currently on a diet', help="Check if the patient is currently on a diet")
    diet_info = fields.Char('Diet info', help="Short description on the diet")
    smoking = fields.Boolean('Smokes')
    smoking_number = fields.Integer('Cigarretes a day')
    ex_smoker = fields.Boolean('Ex-smoker')
    second_hand_smoker = fields.Boolean('Passive smoker', help="Check it the patient is a passive / second-hand smoker")
    age_start_smoking = fields.Integer('Age started to smoke')
    age_quit_smoking = fields.Integer('Age of quitting', help="Age of quitting smoking")
    alcohol = fields.Boolean('Drinks Alcohol')
    age_start_drinking = fields.Integer('Age started to drink ', help="Date to start drinking")
    age_quit_drinking = fields.Integer('Age quit drinking ', help="Date to stop drinking")
    ex_alcoholic = fields.Boolean('Ex alcoholic')
    alcohol_beer_number = fields.Integer('Beer / day')
    alcohol_wine_number = fields.Integer('Wine / day')
    alcohol_liquor_number = fields.Integer('Liquor / day')
    drug_usage = fields.Boolean('Drug Habits')
    ex_drug_addict = fields.Boolean('Ex drug addict')
    drug_iv = fields.Boolean('IV drug user', help="Check this option if the patient injects drugs")
    age_start_drugs = fields.Integer('Age started drugs ', help="Age of start drugs")
    age_quit_drugs = fields.Integer('Age quit drugs ', help="Date of quitting drugs")
    recreational_drugs = fields.One2many( 'oemedical.patient.recreational_drugs', 'patient_id', 'Drugs')
    traffic_laws = fields.Boolean('Obeys Traffic Laws', help="Check if the patient is a safe driver")
    car_revision = fields.Boolean('Car Revision', help="Maintain the vehicle. Do periodical checks - tires,breaks ...")
    car_seat_belt = fields.Boolean('Seat belt', help="Safety measures when driving : safety belt")
    car_child_safety = fields.Boolean('Car Child Safety', help="Safety measures when driving : child seats, proper seat belting, not seating on the front seat, ....")
    home_safety = fields.Boolean('Home safety',  help="Keep safety measures for kids in the kitchen, correct storage of chemicals, ...")
    motorcycle_rider = fields.Boolean('Motorcycle Rider', help="The patient rides motorcycles")
    helmet = fields.Boolean('Uses helmet',  help="The patient uses the proper motorcycle helmet")
    lifestyle_info = fields.Text('Extra Information')
    sexual_preferences = fields.Selection([
        ('h', 'Heterosexual'),
        ('g', 'Homosexual'),
        ('b', 'Bisexual'),
        ('t', 'Transexual'),
        ], 'Sexual Preferences', sort=False)

    sexual_practices = fields.Selection([
        ('s', 'Safe / Protected sex'),
        ('r', 'Risky / Unprotected sex'),
        ], 'Sexual Practices', sort=False)

    sexual_partners = fields.Selection([
        ('m', 'Monogamous'),
        ('t', 'Polygamous'),
        ], 'Sexual Partners', sort=False)

    sexual_partners_number = fields.Integer('Number of sexual partners')

    first_sexual_encounter = fields.Integer('Age first sexual encounter')

    anticonceptive = fields.Selection([
        ('0', 'None'),
        ('1', 'Pill / Minipill'),
        ('2', 'Male condom'),
        ('3', 'Vasectomy'),
        ('4', 'Female sterilisation'),
        ('5', 'Intra-uterine device'),
        ('6', 'Withdrawal method'),
        ('7', 'Fertility cycle awareness'),
        ('8', 'Contraceptive injection'),
        ('9', 'Skin Patch'),
        ('10', 'Female condom'),
        ], 'Anticonceptive Method', sort=False)

    sex_oral = fields.Selection([
        ('0', 'None'),
        ('1', 'Active'),
        ('2', 'Passive'),
        ('3', 'Both'),
        ], 'Oral Sex', sort=False)

    sex_anal = fields.Selection([
        ('0', 'None'),
        ('1', 'Active'),
        ('2', 'Passive'),
        ('3', 'Both'),
        ], 'Anal Sex', sort=False)

    prostitute = fields.Boolean('Prostitute', help="Check if the patient (he or she) is a prostitute")
    sex_with_prostitutes = fields.Boolean('Sex with prostitutes', help="Check if the patient (he or she) has sex with prostitutes")

    sexuality_info = fields.Text('Extra Information')

    cage = fields.One2many('oemedical.patient.cage', 'name', 'CAGE')
