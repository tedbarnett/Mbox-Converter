# Mbox-Converter
Python app to convert email mbox file to markdown format for use in AI and Langchain

In order to make it possible to "talk to yourself" with AI, you first need a reliable source of text that represents your "voice".  One great source for that might be your own Sent Emails over the last few years.  

This app reads through the mbox and cleans it up by...
- Deleting "unsubscribe" emails
- Ignoring file attachments
- Ignoring other forwarded email text (usually preceded with a ">")
- Converting HTML to text
- Writing all of this out into a simple text file

Instructions:
- Export an mbox file from your Sent Emails (using Apple Mail or Google Takeout)
- Pull down the Repo
- Rename the file "RENAME_THIS_config.py" to "config.py"
- Edit this config.py file to include your own OpenAI API key
- Copy your mbox file into this directory and name it "convert-me.mbox"
- Install html2txt (pip install html2txt)
- Run the script mbox-convert.py
- Will take several minutes (depending on size of your mbox file)
- Result will be in the file "converted-mbox.txt"
- Use langchain or other services to make an LLM based on the mbox



This app was built by Ted Barnett, using ChatGPT-4 itself.
