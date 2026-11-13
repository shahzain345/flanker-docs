---
title: Tickets & applications
description: Support tickets with transcripts, and staff applications.
---

## Tickets

Every ticket is a **private thread** in your ticket channel. Only the member,
your support team and flanker can see it. flanker never creates a channel or
edits permissions for a ticket, so it needs only these in the ticket channel:
View Channel, Send Messages in Threads, Create Private Threads, Manage Threads,
Read Message History, Embed Links and Attach Files. Members need **Send
Messages in Threads** there too.

- Post a panel with a button or menu for each ticket type. Run `/setup ticket`
  to create panels and edit every ticket type from Discord, or use the
  [dashboard](https://flanker.wtf/dashboard).
- Each type opens its threads in its own channel, or the panel's channel if you
  don't pick one.
- If the type has an **entry form**, members fill in up to five questions in a
  pop-up before the ticket opens. The answers are the first message.
- Support roles of up to 25 people are added to each new ticket. Bigger teams
  use **Join** on the staff list instead, so a ticket never pulls in hundreds
  of people. They're added quietly, without an "added to the thread" line for
  each person. Anyone with Manage Threads in the ticket channel can also see
  every ticket.
- The thread name shows its state: a green dot when open, yellow when claimed,
  and a lock when closed, then the type's short name, the number and the
  member, like `support-0012 · sam` or `purchase-0013 · alex`. Change the short
  name in `/setup ticket` under the ticket type.
- Staff can claim, add or remove people, and close. Turning on **Claimer only**
  removes the rest of the support team from a ticket once someone claims it.
- Closing locks and archives the thread. The member can still read it, and
  staff can reopen or delete it.
- On close, flanker saves a **transcript** that can be read on
  [flanker.wtf](https://flanker.wtf/transcripts) by the ticket's opener, the
  people who wrote in it, and the server's ticket staff (after signing in with
  Discord). The opener also gets it by DM unless you turn that off. Images
  posted in the ticket are kept with it. Transcripts are deleted automatically
  after one year.

### Report to staff

Members can right-click any message (or long-press on mobile), choose
**Apps**, then **Report to staff**. They can add a reason, and flanker opens a
ticket with a link to the message, who sent it and what it said. Reports open
the first enabled ticket type unless you pick one with **Use for reports** in
`/setup ticket`.

### Staff ticket list

Pick a staff channel in `/setup ticket`, under Ticket settings, and flanker
keeps one message there listing the open tickets. Tickets waiting on a staff
reply come first, then unclaimed, then claimed. Each one has a **Join** button
that adds you to the thread.

### Quiet tickets

When nobody writes in a ticket for 48 hours, flanker warns the member that it
will close and adds a **Keep open** button. If nobody replies within 24 hours,
it closes with a transcript as usual. Change both times, or turn this off, in
Ticket settings. Discord archives threads after a week without messages, and
flanker closes those tickets properly too.

Tickets opened before 12 November 2026 are channels and keep working until
they're closed or deleted.

See `/help module ticket` and the
[VoiceMaster, tickets, applications commands](/commands/voicemaster-tickets-applications/).

## Applications

Run staff or role applications with custom forms.

- Build an application form with your own questions.
- Members apply, and their answers are submitted for review.
- Staff approve or deny, and flanker records the submission.

Configure both on the [dashboard](https://flanker.wtf/dashboard) for a visual
form builder and a live preview.

## Support roles

Each ticket type can have several support roles. Pick them in `/setup ticket`
or on the dashboard under **Managing roles**. Changing them affects new
tickets; people already in a ticket stay in it.

Transcripts use the same Discord-style typography and message layout as dashboard previews. They include attachments, reply references and code formatting without granting public access to private tickets.


## The current ticket workspace

Open **Tickets → Set up tickets → Panels**. Choose one panel, then use **Message & posting** for its destination and message, or **Ticket types** for staff access, the ticket channel and questions. Server defaults and blocked members have their own views. Open and recently closed tickets are under **Activity**.

Drafts remain while you switch views, but you still need to save. Save panel changes before sending the panel again to Discord. Creating or editing a configuration does not silently replace a previously posted panel.

## Review an application

Application review cards keep actions inside the card. Use Accept or Deny for a decision, or their required-reason variants when the applicant needs an explanation. Open ticket starts a follow-up conversation using configured ticket access.

- **Private notes:** staff-only comments stay separate from applicant answers.
- **Request more information:** collect follow-up answers before deciding.
- **Shortlist / On hold:** mark a review stage without accepting or denying.

A review stage does not assign acceptance roles or send a final-decision message. Check reviewer permissions and configured ticket access before relying on the controls.
