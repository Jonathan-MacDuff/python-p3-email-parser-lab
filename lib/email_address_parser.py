import re   

class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses

    

    def parse(self):
        split_pattern = r"[\s,]"
        split_compiler = re.compile(split_pattern)
        split_results = split_compiler.split(self.addresses)
        email_pattern = r"[A-Za-z][A-Za-z0-9/._-]*@[A-z]*.[A-z]{1,}"
        email_compiler = re.compile(email_pattern)
        results = []
        for item in split_results:
            match = email_compiler.search(item)
            if match:
                results.append(match.group())
        sorted_results = sorted(results)
        return sorted_results