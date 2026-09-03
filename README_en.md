
---

## 🎯 About This Project

Near the end of 2025, I started learning about AI agents. I found the topic interesting and decided to explore it on my own.

I know myself: if I don't have somewhere to track my progress, it's easy to lose focus and put things off. I started this repository to keep myself moving, write down what I learn, and make sense of the learning path as I go.

Along the way, I realized I wasn't the only one trying to get into the field. Some people already know how to build software; others are starting without ever having written a line of code.

That is how these notes began to grow into a tutorial.

This guide starts at the beginning. It assumes no prior knowledge of agents, LLMs, or APIs. I break down the code wherever I can so that even a first-time programmer can understand why each line is there.

Still, learning all of this without any programming background can be tough. If you're completely new to code, spend a week or two on the Python basics first: variables, conditions, loops, functions, lists, dictionaries, classes, objects, and error handling. You don't need to master them. A little familiarity will make everything that follows much easier.

I'm learning this as I write it, so this isn't a definitive guide from an expert. Think of it as a set of practical notes from one learner to another, organized around the things that finally made sense to me.

If it helps someone else find their footing, then this repository has done its job. I hope it helps you too.

### ✨ What You Will Learn

- 🔍 <strong>A path through the basics</strong> — a clear starting point if you are not sure where to begin
- 🏗️ <strong>Hands-on practice</strong> — work your way from a simple Q&A script to a working agent
- 🛠️ <strong>A framework of your own</strong> — learn how to build an agent framework by working directly with the OpenAI API
- ⚙️ <strong>Topics beyond the basics</strong> — explore context engineering, memory, protocols, evaluation, and more
- 🚀 <strong>Complete projects</strong> — bring everything together in projects such as an AI travel assistant, or build something entirely your own

## 📖 Contents

The chapters build on one another, so they are best read in order. You will begin with a single model call, then turn it into an ongoing conversation and see how chat history gives an application its “memory.”

| Chapter | Key Topics | Status |
| --- | --- | :---: |
| [Chapter 1: Your First LLM API Call](./Chapter%201%20实现最基础的问答/实现一个最基础的问答.md) | Set up a client, prepare `messages`, call the model, and read its answer from the response | ✅ |
| [Chapter 2: Adding Memory to a Chat Program](./Chapter%202%20带有记忆的问答/带有记忆的问答.md) | Build a continuous terminal chat, manage message history and roles, and learn where this simple form of memory falls short | ✅ |


## 🧰 Learning Resources

| Tutorial | Link |
| --- | --- |
| Datawhale: Hello-Agents | [GitHub repository](https://github.com/datawhalechina/hello-agents) |


## 📄 Research Papers

| Paper | Authors and Year |
| --- | --- |
| [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) | Shunyu Yao et al., 2022 |
