from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local_name = email.split("@")[0].replace('.','')
            domain_name = email.split("@")[1]
            local_name = local_name.split("+")[0] if '+' in local_name else local_name
            unique_emails.add(f"{local_name}@{domain_name}")

        return len(unique_emails)

if __name__ == "__main__":
    solution = Solution()
    emails1 = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    emails2 = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]

    print(solution.numUniqueEmails(emails1))
    print(solution.numUniqueEmails(emails2))