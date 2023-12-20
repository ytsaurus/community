from typing import List, Optional, Dict
from pydantic import BaseModel
import urllib.parse
import yaml


class Sig(BaseModel):
    name: str
    scope: str
    primary_repo: Optional[str]
    tags: List[str]
    chairs: List[str]


class Person(BaseModel):
    name: str
    affiliation: str


class SigData(BaseModel):
    repos: Dict[str, str]
    people: Dict[str, Person]
    sigs: List[Sig]


def main():
    data = SigData(**yaml.safe_load(open("sigs.yaml")))

    """
    | Name | Scope | Issue tags | Chairs |
| ---  | --- | --- | --- |
| k8s operator | k8s operator, best practices of k8s deployment, load balancing | `k8s-operator` | [Maxim Akhmedov](https://github.com/zlobober) <br/> [Grigory Reznikov](https://github.com/gritukan)  |
"""

    print("| Name | Scope | Issue tags | Chairs |")
    print("| ---  | --- | --- | --- |")
    for sig in data.sigs:
        if sig.primary_repo is None:
            assert len(sig.tags) == 0
            tags = ""
        else:
            primary_repo_url = data.repos[sig.primary_repo]
            tags = ", ".join(
                [
                    f"[{tag}]({primary_repo_url}/labels/{urllib.parse.quote_plus(tag)})"
                    for tag in sig.tags
                ]
            )
        chairs = []
        sig.chairs.sort(key=lambda x: data.people[x].name)
        for chair in sig.chairs:
            person = data.people[chair]
            chairs.append(
                f"[{person.name}](https://github.com/{chair}), {person.affiliation}"
            )
        print(f"| {sig.name} | {sig.scope} | {tags} | {' <br /> '.join(chairs)} |")


if __name__ == "__main__":
    main()
