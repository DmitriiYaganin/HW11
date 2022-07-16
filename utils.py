import json

def load_candidates_from_json():
    """
    возвращает список всех кандидатов
    :param:
    :return:
    """
    with open("candidates.json", "r", encoding="utf-8") as f:
        return json.load(f)



def get_candidate(candidate_pk):
    """
    возвращает одного кандидата по его pk
    :param candidate_pk:
    :return:
    """
    for res in load_candidates_from_json():
        if res['pk'] == candidate_pk:
            return res


def get_candidates_by_name(name):
    """
    возвращает кандидатов по имени
    :param candidate_name:
    :return:
    """
    res = []
    for i in load_candidates_from_json():
        if name.lower() in (i['name']).lower():
            res.append(i)
    return res



def get_candidates_by_skill(skill):
    """
    возвращает кандидатов по навыку
    :param skill_name:
    :return:
    """
    res = []
    for i in load_candidates_from_json():
        if skill.lower() in (i['skills']).lower():
            res.append(i)
    return res

