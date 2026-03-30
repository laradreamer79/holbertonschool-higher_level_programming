def generate_invitations(template, attendees):
    """
    Generates invitation files from a template and a list of attendees.

    Args:
        template (str): The invitation template containing placeholders.
        attendees (list): A list of dictionaries with attendee data.
    """

    if not isinstance(template, str):
        print(f"Invalid input: template should be a string but got {type(template).__name__}.")
        return

    if not isinstance(attendees, list):
        print(f"Invalid input: attendees should be a list but got {type(attendees).__name__}.")
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Invalid input: attendees should be a list of dictionaries.")
        return

    if template == "":
        print("Template is empty, no output files generated.")
        return

    if attendees == []:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        name = attendee.get("name") if attendee.get("name") is not None else "N/A"
        event_title = attendee.get("event_title") if attendee.get("event_title") is not None else "N/A"
        event_date = attendee.get("event_date") if attendee.get("event_date") is not None else "N/A"
        event_location = attendee.get("event_location") if attendee.get("event_location") is not None else "N/A"

        invitation = template
        invitation = invitation.replace("{name}", str(name))
        invitation = invitation.replace("{event_title}", str(event_title))
        invitation = invitation.replace("{event_date}", str(event_date))
        invitation = invitation.replace("{event_location}", str(event_location))

        filename = f"output_{index}.txt"

        with open(filename, "w") as file:
            file.write(invitation)