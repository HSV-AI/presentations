![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)
# Replit Agent Presentation - July 23, 2025

## Introduction

Welcome to this presentation on Replit Agent! We'll cover an overview of the Replit Agent, walk through an example of a real-world team actively using Replit Agent as part of their Software Development Lifecycle, and develop an application from scratch.

## From Idea to Software Application

Traditionally, the process of going from idea to a working software application requires technical experience, money, and time.

Limitations of current approaches:
* Require software engineering understanding to do essentially any development
* Low-value in building hyper-personalized applications to solve individual use cases.
* More difficult to iterate quickly on ideas / features
* Difficult to communicate what is technically feasible to non-developers

## New AI Tools

A series of AI Tools have exploded in popularity over the past few months that address these limitations
* Software engineering understanding is offloaded to an LLM
* Hyper-personalized applications can be built very fast (few minutes to hours)
* Rapid iteration through conversational prompting
* Allow non-developers to better communicate through prototype development

Few examples: Lovable, Bolt, Replit Agent

* **Lovable**: Credit-based system, only supports JS/TS (Vite / React), $25/month for "Pro" Tier
* **Bolt**: Token-based system, only supports JS/TS, $20/month for "Pro" Tier
* **Replit**: Credit-based system, supports JS/TS/Python, $25/month for "Pro" Tier ($25 in monthly credits)

All use Claude Sonnet 4. All have Figma, Stripe, Postgres (or Supabase), Github, and LLM integrations. Bolt allows you to import from Lovable and Replit can import from both Bolt and Lovable.

### What is Replit Agent?

AI Agent, leveraging Claude Sonnet 4, to convert conversational prompts into working software

* Replit handles the infrastructure / deployment
* Web apps are built using natural language, with ability to include authorization, databases, object stores, secrets, etc.
* Available 3rd party integrations (OpenAI, Github, Figma, Stripe)

Let's walk through a short example highlighting the platform

## Replit in Real-World

How Replit is being used by Andrew and Team

* Demonstrate built application
* Changes to SDLC
* Changes to communication

## Build an App

Replit Demo on building a workout planner application

Initial prompt for ChatGPT/Gemini:
* Create a software design document for an application that is a daily workout planner. The user should be able to specify what equipment they have and how long of a workout they want to do. Do not include authentication in the initial version of the application. Use Python Flask for the application

## Questions?

Let's open the floor for questions.
