from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            split_names = email.split('@')
            ignored = split_names[0].split('+')
            replaced = ignored[0].replace('.','')
            final = '@'.join([replaced,split_names[1]])
            unique_emails.add(final)
        return len(unique_emails)
    def commented(self, emails: List[str]) -> int:
        # set to only hold unique emails after changing
        unique_emails = set()
        # loop over each string in the arr
        for email in emails:
            # split on the @ to get username and domain separate
            # ie. 'nat.e+w@codingtemple.com' -> ['nat.e+w', 'codingtemple.com']
            split_names = email.split('@')
            # we don't gare about anything after the +, so split again
            # ignored = ['nat.e', 'w']
            ignored = split_names[0].split('+')
            # we only care about items before the '+', so look at idx 0
            # and replace '.' with '' because dots can be ignored
            # replaced = 'nate'
            replaced = ignored[0].replace('.','')
            # join newly formatted username with original email domain
            # final = 'nate@codingtemple.com'
            final = '@'.join([replaced,split_names[1]])
            # add this to the set
            unique_emails.add(final)
        # since set will always be unique, we can just return the len
        return len(unique_emails)