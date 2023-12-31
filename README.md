# Auto Prompt: Generative AI Prompt Autocomplete

This Python script builds prompts for generative AI applications. The goal is to make
prompt engineering easier, by using autocomplete when typing prompts. The autocomplete
corpus can be defined by the user.

**Contents**
1. [Prompt Structure](#1-prompt-structure)
2. [Pharmaceutical Prompts Example](#2-pharmaceutical-prompts-example)
3. [Responsible Use of Data](#3-responsible-use-of-data)
4. [Design Notes / Suggested Improvements](#4-design-notes--suggested-improvements)
4. [References](#5-references)

## 1. Prompt Structure
Please see the below table for the prompt structure used with the Auto Prompt tool:
* The header row has the components of a prompt, written order from left to right

  **NOTE:** In most generative AI prompts, these components are commonly written in separate lines, for human readability

* The second row describes the purpose of each prompt component
* The last row gives an example of each prompt component, taken from the included prompt training data, [pharmaceutical_prompts.csv](./pharmaceutical_prompts.csv)


|Request|Key|Formats|Framing|Shots|
|-------|---|-------|-------|-----|
|The main body of the prompt|The most important word or phrase in the body of the prompt|Specific attributes that the user wants the bot to output|Context or a description of the problem|Example answer content and structure|
|What should a patient know about this drug|Omeprazole (Prilosec)|college level English|I am a pharmacist doing patient consults|Omeprazole is used to treat excess stomach acid in conditions such as non cancerous stomach ulcers, gastroesophageal reflux disease (GERD), active duodenal ulcer, Zollinger-Ellison syndrome and erosive esophagitis. Omeprazole works by blocking gastric acid production and is from the group of medicines called proton pump inhibitors.|

## 2. Pharmaceutical Prompts Example
Included in this repo is training data for building generative AI prompts related to the pharmaceutical industry:
[pharmaceutical_prompts.csv](./pharmaceutical_prompts.csv).

## 3. Responsible Use of Data
The key component of the Auto Prompt tool is actually the training data. Every effort should be made to acquire accurate data from an accountable source. Even more importantly, credit should be given to the providers of the data. The example training data included in [pharmaceutical_prompts.csv](./pharmaceutical_prompts.csv) was sourced from the entities listed in the below [References](#5-references)
section.

## 4. Design Notes / Suggested Improvements
* Most of the time was spent on preparing the training data

## 5. References
* https://docs.python.org/3/howto/curses.html
* [Prompt Structure in Conversations with Generative AI](https://www.nngroup.com/articles/ai-prompt-structure/)
* [ClinCalc.com](https://clincalc.com)'s [Top 250 Pharmaceutical Drugs](https://clincalc.com/Downloads/Top250Drugs-DrugList.pdf)
* [Drugs.com](https://www.drugs.com), for drug interactions
* [McKesson Corporation](https://www.mckesson.com/Pharmaceutical-Distribution/)
* [U.S. Department of Justice, Drug Enforcement Administration](https://www.deadiversion.usdoj.gov/schedules/)
* [FDA List of Authorized Generic Drugs](https://www.fda.gov/drugs/abbreviated-new-drug-application-anda/fda-list-authorized-generic-drugs)