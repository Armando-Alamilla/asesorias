"""
School fields:
name, slug_name, about, courses_offered, verified, is_public
"""

# Python utils
import csv

# Models
from asesorias.schools.models.schools import School


def load_schools(file_name):
    with open(file_name, mode='r') as csvfile:
        readed_file = csv.DictReader(csvfile)

        for row in readed_file:
            school_object = School(**row)
            school_object.save()

            print('Guardando {}'.format(row['slug_name']))
