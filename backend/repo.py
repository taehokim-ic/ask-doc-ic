import asyncio
from models.data_models import *
from sqlalchemy.future import select
from fastapi import HTTPException

PROBABILITY_THRESHOLD = 0.10

async def select_no_category_table(table, session):
    res =  await session.execute(select(table))
    await session.commit()
    if not res:
        raise HTTPException(status_code=404)
    return res

async def select_category_table(table, category, session):
    statement = select(table).where(table.category == category)
    res =  await session.execute(statement)
    await session.commit()
    if not res:
        raise HTTPException(status_code=404)
    return res

async def select_category_module_table(table, session, category="general", module="general"):
    statement = select(table).where(table.category == category).where(table.module == module)
    res =  await session.execute(statement)
    await session.commit()
    if not res:
        raise HTTPException(status_code=404)
    return res

async def add_message(message, session):
    question = Questions(question=message)
    session.add(question)
    await session.commit()
    await session.refresh(question)
    
async def get_intent_data(intent_result, session):
    intent = intent_result['intent']['intentName']
    probability = intent_result['intent']['probability']
    
    link_pair = []
    
    if intent and probability < PROBABILITY_THRESHOLD:
        return link_pair
    elif intent == 'general_accommodation':
        link_pair = await select_no_category_table(GeneralAccommodation, session=session)
    elif intent == 'careers':
        link_pair = await select_no_category_table(Careers, session=session)
    elif intent == 'study_interruption':
        link_pair = await select_no_category_table(StudyInterruption, session=session)
    elif intent == 'crime':
        link_pair = await select_no_category_table(Crime, session=session)
    elif intent == 'finances':
        link_pair = await select_no_category_table(Finances, session=session)
    elif intent == 'doctor':
        link_pair = await select_no_category_table(Doctor, session=session)
    elif intent == 'dental':
        link_pair = await select_no_category_table(Dental, session=session)
    elif intent == "academic_appeal":
        link_pair = await select_no_category_table(AcademicAppeal, session=session)
    elif intent == 'library':
        link_pair = await select_no_category_table(Library, session=session)
    elif intent == 'mental_health':
        link_pair = await select_no_category_table(MentalHealth, session=session)
    elif intent == 'private_housing':
        link_pair = await select_no_category_table(PrivateHousing, session=session)
    elif intent == 'summer_accommodation':
        link_pair = await select_no_category_table(SummerAccommodation, session=session)
    elif intent == 'specific_halls':
        result_slot = intent_result["slots"]
        if len(result_slot) > 0:
            slots = result_slot[0]
            if len(slots) > 0:
                link_pair = await select_category_table(SpecificHalls, slots["value"]["value"], session=session)
    elif intent == 'hall_senior':
        link_pair = await select_no_category_table(HallSenior, session=session)
    elif intent == 'discount':
        link_pair = await select_no_category_table(Discount, session=session)
    elif intent == 'mitigation':
        link_pair = await select_no_category_table(Mitigation, session=session)
    elif intent == 'student_status':
        link_pair = await select_no_category_table(StudentStatus, session=session)
    elif intent == 'societies':
        link_pair = await select_no_category_table(Societies, session=session)    
    elif intent == 'chaplaincy':
        link_pair = await select_no_category_table(Chaplaincy, session=session)
    elif intent == 'travel':
        link_pair = await select_no_category_table(Travel, session=session)
    elif intent == 'exam_revision':
        link_pair = await select_no_category_table(ExamRevision, session=session)                     
    elif intent == 'tuition fees':
        link_pair = await select_no_category_table(TuitionFees, session=session)
    elif intent == 'friends':
        link_pair = await select_no_category_table(Friends, session=session)
    elif intent == 'arithmetic_mark_check':
        link_pair = await select_no_category_table(ArithmeticMarkCheck, session=session)
    elif intent == 'course_info_y1':
        link_pair = await select_category_module_table(CourseInfo, session=session, category="first year")
    elif intent == 'course_info_y2':
        link_pair = await select_category_module_table(CourseInfo, session=session, category="second year")
    elif intent == 'course_info_y3':
        link_pair = await select_category_module_table(CourseInfo, session=session, category="third year")
    elif intent == 'course_info_y4':
        link_pair = await select_category_module_table(CourseInfo, session=session, category="fourth year")
    elif intent == 'docsoc':
        link_pair.append(("DoCSoC", "https://docsoc.co.uk/"))
    elif intent == 'doc':
        link_pair.append(("DoC FAQS", "/2122/questions"))
    else:   # NULL
        pass
    
    return link_pair