from env.models import Action

def grade_easy_spam(action: Action, expected: dict) -> float:
    """Grader for easy_spam task"""
    score = 0.15
    
    if action.label == expected["label"]:
        score += 0.25
    
    if action.priority == expected["priority"]:
        score += 0.25
    
    requires = expected.get("requires", [])
    reply_text = action.reply.lower()
    keyword_hits = sum(1 for kw in requires if kw in reply_text)
    
    if requires:
        ratio = keyword_hits / len(requires)
        score += 0.25 * ratio
    
    # Ensure score is strictly within (0, 1)
    return max(0.01, min(0.99, score))


def grade_medium_meeting(action: Action, expected: dict) -> float:
    """Grader for medium_meeting task"""
    score = 0.15
    
    if action.label == expected["label"]:
        score += 0.25
    
    if action.priority == expected["priority"]:
        score += 0.25
    
    requires = expected.get("requires", [])
    reply_text = action.reply.lower()
    keyword_hits = sum(1 for kw in requires if kw in reply_text)
    
    if requires:
        ratio = keyword_hits / len(requires)
        score += 0.25 * ratio
    
    # Ensure score is strictly within (0, 1)
    return max(0.01, min(0.99, score))


def grade_hard_multi(action: Action, expected: dict) -> float:
    """Grader for hard_multi task"""
    score = 0.15
    
    if action.label == expected["label"]:
        score += 0.25
    
    if action.priority == expected["priority"]:
        score += 0.25
    
    requires = expected.get("requires", [])
    reply_text = action.reply.lower()
    keyword_hits = sum(1 for kw in requires if kw in reply_text)
    
    if requires:
        ratio = keyword_hits / len(requires)
        score += 0.25 * ratio
    
    # Ensure score is strictly within (0, 1)
    return max(0.01, min(0.99, score))


def grade_support_request(action: Action, expected: dict) -> float:
    """Grader for support_request task"""
    score = 0.15
    
    if action.label == expected["label"]:
        score += 0.25
    
    if action.priority == expected["priority"]:
        score += 0.25
    
    requires = expected.get("requires", [])
    reply_text = action.reply.lower()
    keyword_hits = sum(1 for kw in requires if kw in reply_text)
    
    if requires:
        ratio = keyword_hits / len(requires)
        score += 0.25 * ratio
    
    # Ensure score is strictly within (0, 1)
    return max(0.01, min(0.99, score))


GRADERS = {
    "easy_spam": grade_easy_spam,
    "medium_meeting": grade_medium_meeting,
    "hard_multi": grade_hard_multi,
    "support_request": grade_support_request,
}
