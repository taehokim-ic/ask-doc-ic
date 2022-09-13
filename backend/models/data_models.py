from typing import Optional
from sqlmodel import SQLModel, Field

class NoCatergory(SQLModel):
    id: Optional[int] = Field(primary_key=True)
    keyword: str = Field(index=True)
    link: str
    
class Catergory(SQLModel):
    id: Optional[int] = Field(primary_key=True)
    category: str = Field(index=True)
    keyword: str
    link: str
    
class CatergoryModule(SQLModel):
    id: Optional[int] = Field(primary_key=True)
    category: str = Field(index=True)
    module: str
    keyword: str
    link: str    
    
class Questions(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    question: str

class AcademicAppeal(NoCatergory, table=True):
    pass
    
class Careers(NoCatergory, table=True):
    pass

class Chaplaincy(NoCatergory, table=True):
    pass

class Societies(NoCatergory, table=True):
    pass

class Crime(NoCatergory, table=True):
    pass

class Dental(NoCatergory, table=True):
    pass

class Discount(NoCatergory, table=True):
    pass

class Doctor(NoCatergory, table=True):
    pass
    
class HallSenior(NoCatergory, table=True):
    pass

class Finances(NoCatergory, table=True):
    pass

class Library(NoCatergory, table=True):
    pass

class Mitigation(NoCatergory, table=True):
    pass

class GeneralAccommodation(NoCatergory, table=True):
    pass

class StudentStatus(NoCatergory, table=True):
    pass
    
class MentalHealth(NoCatergory, table=True):
    pass

class PrivateHousing(NoCatergory, table=True):
    pass

class SpecificHalls(Catergory, table=True):
    pass

class SummerAccommodation(NoCatergory, table=True):
    pass

class TuitionFees(NoCatergory, table=True):
    pass

class Travel(NoCatergory, table=True):
    pass

class ExamRevision(NoCatergory, table=True):
    pass

class CourseInfo(CatergoryModule, table=True):
    pass

class StudyInterruption(NoCatergory, table=True):
    pass

class Friends(NoCatergory, table=True):
    pass

class ArithmeticMarkCheck(NoCatergory, table=True):
    pass
