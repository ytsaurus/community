# YTsaurus community

Welcome to YTsaurus community!

This document describes the process, under which the YTsaurus is developed. Use it as an entry point for contributing to the project.

## Repositories

Currently, there are following repositories within YTsaurus community:

* [ytsaurus](https://github.com/ytsaurus/ytsaurus) – the main repository, which contains the server-side code of YTsaurus and official SDKs.
* [ytsaurus-cpp-sdk](https://github.com/ytsaurus/ytsaurus-cpp-sdk) - the C++ SDK for YTsaurus.
* [ytsaurus-ui](https://github.com/ytsaurus/ytsaurus-ui) – the UI repository
* [ytsaurus-k8s-operator](https://github.com/ytsaurus/ytsaurus-k8s-operator) – the Kubernetes operator for YTsaurus
* [ytsaurus-terraform-provider](https://github.com/ytsaurus/ytsaurus-terraform-provider) — the Terraform provider for YTsaurus

## Governance

Primary goals that we are aiming to achieve by the current governance model are:
* Safety – YTsaurus evolves in a safe and backward compatible (to a reasonable extent) way, allowing users to upgrade YTsaurus installations with confidence.
* Liveness – development process is built in such manner that developers are able to predictably make progress on their work; PRs are reviewed, and new features are released in a timely manner.
* Transparency – developers with various affiliations are able to participate in the development process on equal terms, receive necessary information and influence the decision making.

## SIGs

YTsaurus domain area is quite wide, so it is divided into several subprojects. Each subproject is developed and maintained by its own team, which is called Special Interest Group (SIG).

Each SIG has the following attributes:
* **Scope** – a list of subprojects that are under the SIG's responsibility.
* **Chairs** – a list of people who are organizing the SIGs activity and facilitating the decision making process.
* **Members** – a list of people who are actively contributing to the SIG's activity.
* **Communication channels** – a list of communication channels that are used by the SIG. Currently, we use Telegram chats and Zoom meetings for communication.

The list of SIGs with their scopes and chairs is available in the [SIGs.md](SIGs.md) document.

## Getting involved

Currently, all YTsaurus SIGs are private and are by invitation from chairs only. 

A good way to become a member of a SIG is to start contributing to the SIG's subproject. Have a look at the list of open issues in one of our repositories; issues marked with the `help wanted` label are a good place to start. If you managed to make a few contributions and would like to become a member of the SIG, or you have other solid reasons to join the SIG, please contact one of the SIG's chairs. Also, do not hesitate to discuss your ideas and proposals in one of our public community chats:

* https://t.me/ytsaurus (English)
* https://t.me/ytsaurus_ru (Russian)

