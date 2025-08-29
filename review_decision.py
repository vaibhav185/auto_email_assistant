def needs_review(summary, priority, reply):
    # Simple rule-based confidence filter
    if priority.lower() == "high" and len(reply) < 20:
        return True
    if "not sure" in reply.lower():
        return True
    return False
