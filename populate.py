from sqlmodel import Session

from backend.db.db import engine
from backend.models.data_models import *
import csv

def create_no_category_db(file_name: str, table):
    with Session(engine) as session:
        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0
            for row in csv_reader:
                print(row)
                if line_count != 0:
                    session.add(table(keyword=row[0], link=row[1]))
                line_count = 1
        session.commit()
                
def create_category_db(file_name: str, table):
    with Session(engine) as session:
        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    session.add(table(category=row[0], keyword=row[1], link=row[2]))
                line_count = 1
        session.commit()
        
def create_category_module_db(file_name: str, table: SQLModel):
        with Session(engine) as session:
            with open(file_name) as csv_file:
                csv_reader = csv.reader(csv_file)
                line_count = 0
                for row in csv_reader:
                    if line_count != 0:
                        session.add(table(category=row[0], module=row[1], keyword=row[2], link=row[3]))
                    line_count = 1
            session.commit()
            
if __name__ == "__main__":
    create_no_category_db("./CSV/careers.csv", Careers)
    create_no_category_db("./CSV/crime.csv", Crime)
    create_no_category_db("./CSV/dental.csv", Dental)
    create_no_category_db("./CSV/doctor.csv", Doctor)            
    create_no_category_db("./CSV/hall_senior.csv", HallSenior)
    create_no_category_db("./CSV/finances.csv", Finances)
    create_no_category_db("./CSV/library.csv", Library)
    create_no_category_db("./CSV/general_accommodation.csv", GeneralAccommodation)
    create_no_category_db("./CSV/mental_health.csv", MentalHealth)
    create_no_category_db("./CSV/private_housing.csv", PrivateHousing)
    create_no_category_db("./CSV/tuition_fees.csv", TuitionFees)
    create_no_category_db("./CSV/summer_accommodation.csv", SummerAccommodation)
    create_category_db("./CSV/specific_halls.csv", SpecificHalls)
    create_no_category_db("./CSV/travel.csv", Travel)
    create_no_category_db("./CSV/student_status.csv", StudentStatus)
    create_no_category_db("./CSV/mitigation.csv", Mitigation)
    create_no_category_db("./CSV/chaplaincy.csv", Chaplaincy)
    create_no_category_db("./CSV/club_societies.csv", Societies)
    create_no_category_db("./CSV/discount.csv", Discount)
    create_no_category_db("./CSV/exam_revision.csv", ExamRevision)
    create_category_module_db("./CSV/course_info.csv", CourseInfo)
    create_no_category_db("./CSV/study_interruption.csv", StudyInterruption)
    create_no_category_db("./CSV/academic_appeal.csv", AcademicAppeal)
    create_no_category_db("./CSV/friends.csv", Friends)
    create_no_category_db("./CSV/arithmetic_mark_check.csv", ArithmeticMarkCheck)
