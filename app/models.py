
from dataclasses import dataclass
from typing import Optional


@dataclass
class Group:
    group_id: int
    student1: str
    student2: str
    student3: str
    student4: Optional[str]


group1 = Group(
    group_id=1,
    student1="00123456",
    student2="00123452",
    student3="00123453",
    student4="00123451",
)

group2 = Group(
    group_id=2,
    student1="20123456",
    student2="20123452",
    student3="20123453",
    student4="20123451",
)

group3 = Group(
    group_id=3,
    student1="02123456",
    student2="04123452",
    student3="03123453",
    student4="01123451",
)
        

groups = [group1, group2] # group3]