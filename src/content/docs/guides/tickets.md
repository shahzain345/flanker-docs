---
title: Tickets & applications
description: Support tickets with transcripts, and staff applications.
---

## Tickets

flanker runs a full support-ticket system: a panel members click to open a
private ticket channel, with staff handling and transcripts.

- Create a ticket panel with a button members press to open a ticket.
- Staff can claim, add or remove people, and close tickets.
- On close, flanker saves a **transcript** that can be read on
  [flanker.wtf](https://flanker.wtf/transcripts) by the ticket's opener, the
  people who wrote in it, and the server's ticket staff (after signing in with
  Discord). Images posted in the ticket are kept with it. Transcripts are
  deleted automatically after one year.

See `,help ticket` and the
[VoiceMaster, tickets, applications commands](/commands/voicemaster-tickets-applications/).

## Applications

Run staff or role applications with custom forms.

- Build an application form with your own questions.
- Members apply, and their answers are submitted for review.
- Staff approve or deny, and flanker records the submission.

Configure both on the [dashboard](https://flanker.wtf/dashboard) for a visual
form builder and a live preview.

## Multiple staff and viewer roles

Expand a ticket option on the dashboard and select any required **Managing roles** and **View-only roles**. Each option can use several roles in either list. Managers handle the ticket; viewers can read without replying or gaining ticket-management commands. A role selected in both lists is treated as a manager. Existing Support roles remain compatible.

The command equivalent is `,ticket option set Support 1 manage @Support @SeniorSupport` or `,ticket option set Support 1 view @Observers @Auditors`. Use `none` to clear a list. These channel permissions apply to newly opened tickets; changing an option does not rewrite existing ticket channels.

Transcripts use the same Discord-style typography and message layout as dashboard previews. They include attachments, reply references and code formatting without granting public access to private tickets.


## The current ticket workspace

Open **Tickets → Set up tickets → Panels**. Choose one panel, then use **Message & posting** for its destination and message, or **Ticket types** for staff access, categories and questions. Server defaults and blocked members have their own views. Open and recently closed tickets are under **Activity**.

Drafts remain while you switch views, but you still need to save. Save panel changes before sending the panel again to Discord. Creating or editing a configuration does not silently replace a previously posted panel.

## Review an application

Application review cards keep actions inside the card. Use Accept or Deny for a decision, or their required-reason variants when the applicant needs an explanation. Open ticket starts a follow-up conversation using configured ticket access.

- **Private notes:** staff-only comments stay separate from applicant answers.
- **Request more information:** collect follow-up answers before deciding.
- **Shortlist / On hold:** mark a review stage without accepting or denying.

A review stage does not assign acceptance roles or send a final-decision message. Check reviewer permissions and configured ticket access before relying on the controls.
