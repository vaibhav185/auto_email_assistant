from email_utils import fetch_latest_emails
from chains.summarize_chain import get_summarize_chain
from chains.classify_chain import get_classify_chain
from chains.reply_chain import get_reply_chain
from review_decision import needs_review

def main():
    emails = fetch_latest_emails()
    summarize_chain = get_summarize_chain()
    classify_chain = get_classify_chain()
    reply_chain = get_reply_chain()

    for email_data in emails:
        content = email_data["body"]
        summary = summarize_chain.run(email_content=content)
        priority = classify_chain.run(email_content=content)
        reply = reply_chain.run(email_content=content)
        review = needs_review(summary, priority, reply)

        print("From:", email_data["from"])
        print("Subject:", email_data["subject"])
        print("Summary:", summary)
        print("Priority:", priority)
        print("Draft Reply:", reply)
        print("Requires Review:", review)
        print("=" * 40)

if __name__ == "__main__":
    main()
