# Facebook Contact Exporter

Say you want to export your Facebook contact information into your Google contacts, or anywhere else.
Unfortunately, Facebook does its best to make it hard for you to do this, but there are ways around
Facebook's restrictions. You've come to the right place.

This guide will let you export the following attributes from your Facebook friends: name, email
addresses, location (current), hometown, birthday, workplace, title, website, facebook ID, and notes.
As of 5/5/2014, there's no way to import phone numbers or any other details not listed above.

Also, there is no single way to export all the attributes mentioned above. The name and email addresses
can be exported using one method, and the rest can be exported using a different one. Details in the
sections below. Enjoy.

## Export names and email addresses, via Yahoo

The only known way to export your friends' email addresses is through Yahoo:

1. Create a Yahoo mail account.
2. Go to the Contacts section and click on *Import Contacts*. Follow the steps and your Facebook friends will
be added to your Yahoo contacts. Only their **name** and **email address(es)** will be imported. You'll end up
with something like this:

![Yahoo screenshot](https://github.com/ipince/facebook-contact-exporter/raw/master/yahoo_shot.png "Yahoo screenshot")

Next, you'll want to export your Yahoo contacts into a csv file so you can import it elsewhere. Unfortunately,
Yahoo doesn't allow you to do this (if you try to export, it will only export contacts you've added yourself,
not those you imported from Facebook). But there's a workaround:

1. Click on *Actions -> Print All...* On the popup that appears, select *Your entire Address Book* and the
*Detailed view* layout and click on *Print*.
2. A new tab will be opened and a print dialog will come up. Go ahead and **cancel** the print dialog. You'll
be left with the open tab displaying your contact info, looking like this:
![Printed contacts tab](https://github.com/ipince/facebook-contact-exporter/raw/master/yahoo_printed.png "Printed contacts tab")

3. Hightlight the entire text on the page, like in the screenshot below. Copy it and paste it into a notepad, or
vim, or any text editor. The file should look like the sample file `sample_printed_contacts.txt` in this repo.
![Highlighted contacts](https://github.com/ipince/facebook-contact-exporter/raw/master/yahoo_highlighted.png "Highlighted contacts")

4. Run `printed-contacts-to-csv.py > import.csv` and you'll see an output file named `import.csv`.
There's an example of how that file will look like in this repo too (`sample_import.csv`).

That's it! Now you can import that file into Google contacts, or Outlook, or wherever you want.

## Export the rest of your friends info, via [friendstogmail](http://www.friendstogmail.com)

[friendstogmail.com](http://www.friendstogmail.com) is a page that allows you to login with Facebook and it will
generate a list of your friends' contact info (only the info that is made public by them).
The attributes exported this way includes name, location, hometown, birthday, workplace, title, facebook ID, and
notes. (The *notes* attribute are notes that your friends may have written about themselves, which I don't find
particularly useful). This method does **not** include email or phone numbers.

You can copy/paste the generate list into a text file (or Excel) and import it to wherever you want.

## A note on importing into Google Contacts

For some reason, the format used to import to Google contacts is very specific. The simplest way I've found to
avoid certain columns to be included in the *Notes* section of Google contacts is to use Outlook-style headers.
The script mentioned above (`printed-contacts-to-csv.py`) already does this for the Yahoo-exported details.
More information on the Outlook header titles [here](http://bevhoward.com/GoogleSync.htm) and a discussion on
importing to Google contacts [here](https://productforums.google.com/forum/#!topic/gmail/ZaIARUAhTWo).

Another caveat is that once you import your contacts to Google, you'll want to merge them (since you probably
already had some friends as your contacts before you imported them from Facebook). Google will merge based on
names and/or email addresses. When merging, be mindful of three things: (1) your friend's Facebook name might
be different than the name you gave them on your Google contacts, so Google might not be able to merge them
automatically; (2) be careful with people that have the same name but are different people (e.g. father/son names),
as Google will try to merge them; and (3) sometimes Google will ignore middle names when merging, so a "Jose
Manuel Ramos" may become "Jose Ramos", which might be undesirable, so you might want to merge those manually.
