from env.models import Action

def grade_easy_spam(action: Action, expected: dict) -> float:
    """Grader for easy_spam task"""
    score = 0.1
    
    if action.label == expected["label"]:
        score += 0.3
    
    if action.priority == expected["priority"]:
        score += 0.2
    
    requires = expected.get("requires", [])
    reply_text = action.reply.lower()
    keyword_hits = sum(1 for kw in requires if kw in reply_text)
    
    if requires:
        ratio = keyword_hits / len(requires)
        score += 0.3 * ratio
    
    return score


def grade_medium_meeting(action: Action, expected: dict) -> float:
    """Grader for medium_meeting task"""
    score = 0.1
    
    if action.label == expected["label"]:
        score += 0.3
    
    if action.priority == expected["priority"]:
        score += 0.2
    
    requires = expected.get("requires", [])
    reply_text = action.reply.lower()
    keyword_hits = sum(1 for kw in requires if kw in reply_text)
    
    if requires:
        ratio = keyword_hits / len(requires)
        score += 0.3 * ratio
    
    return score


def grade_hard_multi(action: Action, expected: dict) -> float:
    """Grader for hard_multi task"""
    score = 0.1
    
    if action.label == expected["label"]:
        score += 0.3
    
    if action.priority == expected["priority"]:
        score += 0.2
    
    requires = expected.get("requires", [])
    reply_text = action.reply.lower()
    keyword_hits = sum(1 for kw in requires if kw in reply_text)
    
    if requires:
        ratio = keyword_hits / len(requires)
        score += 0.3 * ratio
    
    return score


GRADERS = {
    "easy_spam": grade_easy_spam,
    "medium_meeting": grade_medium_meeting,
    "hard_multi": grade_hard_multi,
}
