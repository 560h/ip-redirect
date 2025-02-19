import json
import random

# List of websites to redirect to
redirect_urls = [
    'https://www.facebook.com',
    'https://www.discord.com',
    'https://www.youtube.com',
    'https://www.roblox.com',
    'https://www.instagram.com',
    'https://www.github.com',
    'https://www.vercel.com'
]

def handler(event, context):
    # Try to get the user's IP
    user_ip = event.get('headers', {}).get('X-Forwarded-For', 'Unknown IP')
    if user_ip == 'Unknown IP':
        print("Warning: Unable to retrieve IP.")
    
    # Pick a random website from the list
    redirect_url = random.choice(redirect_urls)

    # Print the IP and the site they're being redirected to
    print(f"User IP: {user_ip} redirected to: {redirect_url}")

    # Return a response to redirect the user
    return {
        'statusCode': 302,
        'headers': {
            'Location': redirect_url
        },
        'body': json.dumps({'message': 'Redirecting...'})
    }
