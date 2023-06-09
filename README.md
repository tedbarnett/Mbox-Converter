# Mbox-Converter
Python app to convert email mbox file to text/markdown format for use in AI and Langchain

In order to make it possible to "talk to yourself" with AI, you first need a reliable source of text that represents your "voice".  One great source for that might be your own Sent Emails over the last few years.  

This app reads through an mbox and cleans it up by...
- Deleting "unsubscribe" emails
- Ignoring file attachments
- Ignoring other forwarded email text (usually preceded with a ">")
- Converting HTML to text
- Writing all of this out into a simple text file

Instructions:
- Export an mbox file from your Sent Emails (using Apple Mail or Google Takeout)
- Rename that mbox file "convert-me.mbox"
- Rename the file "RENAME_THIS_config.py" to "config.py"
- Edit this config.py file: change the string "tedsmith" to any text string that will reliably appear in your "from:" email address
- Copy your mbox file into the folder "mbox-source" and make sure it is named "convert-me.mbox"
- Install html2txt (in Terminal: "pip install html2txt")
- Run the script mbox-convert.py
- Will take several minutes (depending on size of your mbox file)
- Result will be in the file "converted-mbox.md" (can open with any text editor to review)
- Use langchain or other services to make an LLM based on the mbox



This app was built by Ted Barnett, using ChatGPT-4 itself.
