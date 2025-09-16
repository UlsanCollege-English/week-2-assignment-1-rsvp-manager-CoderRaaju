from typing import List, Tuple


def dedupe_emails_case_preserve_order(emails: List[str]) -> List[str]:
    """Return a new list with duplicate emails removed, preserving first seen.

    Treat emails case-insensitively ("ALICE@x.com" == "alice@x.com").
    Keep the first form you saw.

    Ignore entries that do not contain an '@' character.
    """
    seen = set()
    result = []
    for email in emails:
        if "@" not in email:   # skip invalid
            continue
        lower_email = email.lower()
        if lower_email not in seen:
            seen.add(lower_email)
            result.append(email)
    return result


def first_with_domain(emails: List[str], domain: str) -> int | None:
    """Return the index of the first email whose domain matches `domain`.

    Examples:
        emails=["a@x.com","b@y.com"], domain="y.com" -> 1
        no match -> None
    Comparison is case-insensitive.
    """
    domain = domain.lower()
    for idx, email in enumerate(emails):
        if "@" not in email:
            continue
        _, email_domain = email.split("@", 1)
        if email_domain.lower() == domain:
            return idx
    return None


def domain_counts(emails: List[str]) -> List[Tuple[str, int]]:
    """Return (domain, count) pairs sorted by domain (A..Z), case-insensitive.

    Skip malformed entries without an '@'.
    Example: ["a@x.com","b@x.com","c@y.com"] -> [("x.com", 2), ("y.com", 1)]
    """
    counts = {}
    for email in emails:
        if "@" not in email:
            continue
        _, domain = email.split("@", 1)
        domain_lower = domain.lower()
        counts[domain_lower] = counts.get(domain_lower, 0) + 1

    return sorted(counts.items(), key=lambda x: x[0].lower())
