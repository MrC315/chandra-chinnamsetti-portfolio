# Employee Request Approval Flow

## Overview

This Power Automate flow automates the employee request approval process for the Employee Directory application. The workflow is triggered whenever a new employee request is created in Microsoft Dataverse.

The flow routes the request to the designated approver, updates the request status based on the approval outcome, and sends email notifications to the requester.

---

## Workflow

1. Employee submits a request through the Power Apps application.
2. A new Employee Request record is created in Dataverse.
3. Power Automate is triggered automatically.
4. An approval request is sent to the designated manager.
5. The manager approves or rejects the request.
6. The request status is updated in Dataverse.
7. A notification email is sent to the requester with the approval outcome.

---

## Technologies

- Microsoft Power Automate
- Microsoft Dataverse
- Microsoft Power Apps
- Microsoft Approvals
- Microsoft Outlook

---

## Key Features

- Automated approval workflow
- Dataverse event trigger
- Manager approval process
- Approval and rejection branching
- Automatic status updates
- Email notifications
- Enterprise workflow automation

---

## Workflow Components

- Dataverse Trigger
- Approval Request
- Approval Decision
- Conditional Logic
- Dataverse Record Update
- Email Notification

---

## Business Benefits

- Eliminates manual approval tracking
- Standardizes employee request processing
- Improves response time
- Provides request status visibility
- Demonstrates low-code business process automation

---

**Author:** Chandra Chinnamsetti
