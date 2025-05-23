class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for email in emails:
            local, domain = email.split('@')  # separate it into local, domain

            # delete after '+'
            if '+' in local:
                local = local[:local.index('+')]

            # delete '.'
            local = local.replace('.', '')

            # make unique email
            cleaned_email = local + '@' + domain
            unique_emails.add(cleaned_email)

        return len(unique_emails)