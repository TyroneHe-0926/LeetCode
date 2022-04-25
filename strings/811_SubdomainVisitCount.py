from typing import List
from collections import defaultdict, deque

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_map = defaultdict(int)
        for domain in cpdomains:
            count, domains = domain.split(" ")
            domains = deque(domains.split('.'))
            while domains:
                domain_map[".".join(domains)] += int(count)
                domains.popleft()
        return [f'{domain_count} {domain_name}' for domain_name, domain_count in domain_map.items()]