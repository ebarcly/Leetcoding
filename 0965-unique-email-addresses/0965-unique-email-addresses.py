class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniques = set()  # store unique emails on a set

        for email in emails:  # loop through emails
            local, domain = email.split("@")  # isolate parts to apply rules
            local = local.replace(".", "")  # replace dots for empty spaces
            local = local.split("+")[0]  # ignore characters after the "+" sign (if one)
            email = f"{local}@{domain}"  # concatenate both parts
            uniques.add(email)  # add them to the set
        return len(uniques)  # the size of the set should be equal to the unique emails