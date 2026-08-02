# Employee Request Approval Flow - Screenshots

This folder contains screenshots demonstrating the complete Power Automate approval workflow used by the Employee Directory application.

## Screens Included

### Flow Overview

Illustrates the complete approval workflow from request creation through final notification.

---

### Dataverse Trigger

Shows the automated trigger that starts the workflow whenever a new Employee Request record is created.

---

### Manager Approval

Displays the approval action that routes employee requests to the designated approver.

---

### Approval Decision

Shows the conditional logic that evaluates whether the request has been Approved or Rejected.

---

### Dataverse Update

Illustrates how the Employee Request record is automatically updated with the latest request status.

---

### Email Notification

Shows the automated email notification sent to the requester after the approval decision.

---

## Workflow Summary

```
Power Apps
      │
      ▼
Dataverse
      │
      ▼
Power Automate
      │
      ▼
Manager Approval
      │
 ┌────┴────┐
 │         │
Approve  Reject
 │         │
 ▼         ▼
Update Dataverse
 │
 ▼
Requester Notification
```

---

## Technologies

- Microsoft Power Automate
- Microsoft Dataverse
- Microsoft Power Apps
- Microsoft Approvals
- Microsoft Outlook

---

## Learning Outcomes

This project demonstrates:

- Event-driven workflow automation
- Dataverse integration
- Conditional business logic
- Approval process automation
- Email notification workflows
- Enterprise application integration
- Low-code process orchestration

---

**Project Author:** Chandra Chinnamsetti

**Purpose:** Portfolio project demonstrating enterprise workflow automation using Microsoft Power Platform.
