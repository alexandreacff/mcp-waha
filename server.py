from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("WAHA Server")

# Constants
WAHA_BASE_URL = "http://localhost:3000"

# Contacts resource - pre-loaded contact information
contacts = {
    "joão": "+556281974011",
    "alexandre": "+556281974011",
    "andressa": "+556281974011"
}


@mcp.resource(f"{WAHA_BASE_URL}/contatos")
def get_contacts():
    """Return the list of contacts."""
    return contacts

async def send_message(phone_number: str, message: str) -> str:
    """Send a WhatsApp message through WAHA server.
    
    Args:
        phone_number: International format phone number (e.g. +5511XXXXXXXX)
        message: Message text to be sent
    """
    # Format the phone number to WhatsApp format @c.us

    chat_id = f"{phone_number.replace('+', '')}@c.us"
        
    url = f"{WAHA_BASE_URL}/api/sendText"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "chatId": chat_id,
        "text": message,
        "session": "default"
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, json=data, headers=headers, timeout=60.0)
            response.raise_for_status()
            result = response.json()
            return f"{result}: Message sent successfully to {phone_number}"

        except Exception as e:
            return f"Error sending message: {str(e)}"

@mcp.tool()
async def send_message_with_contacts(phone: str = "", name: str = "", message: str = "") -> str:
    """Send message using a name or phone number."""
    if not phone:
        phone = contacts.get(name.lower())
        if not phone:
            return f"Number for '{name}' not found."
    return await send_message(phone, message)


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')