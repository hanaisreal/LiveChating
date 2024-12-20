# LiveChating
This project is a simple live chat application using FastAPI for the backend and Streamlit for the frontend. Users can send and receive messages in real-time.

<img width="1512" alt="스크린샷 2024-11-23 오전 1 08 11" src="https://github.com/user-attachments/assets/842cfbb0-39c7-4adb-852e-0f2854192b2f">



# Live Chat Application

A simple live chat application built with **Streamlit** for the frontend and **FastAPI** for the backend. This application allows users to join a chat room, send messages, and view messages from other users in real-time.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
  - [1. Start the Backend Server](#1-start-the-backend-server)
  - [2. Launch the Streamlit Frontend](#2-launch-the-streamlit-frontend)

## Features

- **Real-Time Chat:** Send and receive messages in real-time.
- **User Authentication:** Simple username-based login.
- **URL Detection:** Automatically converts URLs in messages to clickable links.
- **Responsive UI:** User-friendly interface with styled message bubbles.



## Prerequisites

- **Python 3.7+** installed on your machine.
- **pip** package manager.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/live-chat-app.git
   cd live-chat-app


## running-the-application
### 1. Start the Backend Server

Run the following command in the terminal:

    uvicorn backend:app --reload --host 0.0.0.0 --port 8000


### 2-launch-the-streamlit-frontend
    streamlit run app.py 
