{

    'name': 'OeMedical : Module Data',
    'version': '1.0',
    'author': "OeMEdical Team",
    'category': 'Generic Modules/Others',
    'depends': ['oemedical'],
    'application': True,
    'description': """

About OeMedical Data
---------------------

Core Data for oemedical, is kept as a separate module to overcome need of
localizing core data.

    
""",
    "website": "http://launchpad.net/oemedical",
    "licence": "AGPL v3",
    "data": [
        'data/recreational_drugs.xml',
        'data/disease_genes.xml',
        'data/medicament_categories.xml',
        'data/WHO_products.xml',
        'data/WHO_list_of_essential_medicines.xml',
        'data/health_specialties.xml',
        'data/ethnic_groups.xml',
        'data/occupations.xml',
        'data/dose_units.xml',
        'data/drug_routes.xml',
        'data/medicament_form.xml',
        'data/medication_frequencies.xml',
        'data/disease_categories.xml',
        'data/diseases.xml',
    ],
    "demo": [

    ],
    'test':[
            
    ],
    'css': [

    ],
    'js': [

    ],
    'qweb': [

    ], 
    "active": False
}
