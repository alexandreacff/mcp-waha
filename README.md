# 💬 WhatsApp MCP Server (FastMCP + Waha API)

This project implements a WhatsApp messaging server using [MCP](https://modelcontextprotocol.io/) and [Waha](https://waha.devlike.pro/), demonstrating its integration with Claude. It provides a modular set of tools to send messages directly to phone numbers or named contacts.

## ⚙️ Installation & Setup

### Prerequisites: WAHA Setup

Before running this server, you need to install and set up WAHA:

**Step-by-Step guide**
On this page you're going to install and run WAHA, authenticate the client using QR code, and send your first message to WhatsApp using API!

Follow the detailed instructions at: [Quick Start WAHA](https://waha.devlike.pro/docs/overview/quick-start/)

### Starting the Server

1. **Start your Waha server** (default port `3000`) with a running WhatsApp session.

2. **Test the server**:

   ```bash
   python test_API.py
   ```

## 🤖 Claude Desktop Integration

1. **Install Claude Desktop**: Download and install [Claude Desktop](https://claude.ai/download).

2. **Configure the server**: Refer to the [MCP Server documentation](https://modelcontextprotocol.io/quickstart/server) for setting up the server.
   
3. To start the server:
   
    ```bash
    uv run server.py
    ```
The application can be used with any client compatible with the MCP protocol.

## 📝 Usage Guide

### Resource: `/contatos`

Get the list of pre-loaded contacts.

### Tool: `send_message`

Send a WhatsApp message through WAHA server.


## Images

![](images/nome.png)
![](images/numero.png)
