Postmortem Report - Incident at www.kwiqify.com
Summary

On January 15, 2024, at 9:24 PM East African Time (EAT), the error tracking tool (Rollbar) reported a sudden spike in errors on the live production server of www.kwiqify.com. The issue critically impacted the website's functionality, prompting our team to switch the site to maintenance mode at 9:28 PM EAT. The root cause was identified as a database failure resulting from an incorrectly written script during a planned update. The incident was fully resolved, and the website was back in operation by 10:23 PM EAT.
Timeline

    9:23 PM EAT: The production database update was completed.
    9:24 PM EAT: Rollbar detected a significant spike in errors.
    9:26 PM EAT: Investigation initiated by checking logs for the cause.
    9:28 PM EAT: Website switched to maintenance mode.
    9:37 PM EAT: Task to restore the production database initiated.
    9:43 PM EAT: Optimization of Sidekiq workers for faster database restoration.
    9:55 PM EAT: Maintenance mode turned off, 80% of products restored.
    10:23 PM EAT: Production database fully restored, incident resolved.

Root Cause

During a planned update to the production database, an incorrectly written script led to the removal of a significant number of products from the item_datafeed table. This table contains URLs leading to retailers' online stores.
Resolution and Recovery

    9:24 PM PT: Team received alerts from Rollbar, investigation commenced.
    9:26 PM PT: Logs revealed a production database failure as the cause.
    9:28 PM PT: Website moved to maintenance mode.
    9:37 PM PT: Task to restore production database initiated.
    9:43 PM PT: Sidekiq workers optimized for faster database restoration.
    9:55 PM PT: Maintenance mode turned off, 80% of products restored.
    10:23 PM PT: Production database fully restored, website operational.

Corrective and Preventive Measures

After a thorough analysis, the team has identified measures to prevent similar incidents in the future:

    Testing on Staging Server: Despite relying heavily on tests, all changes related to database updates will undergo testing on the staging server before deployment on the production server.
    Regular Database Backups: Implementing regular backups of all project databases to facilitate easy rollback in case of incidents. Additionally, introducing database backups before major changes.
    Increased Test Coverage: Enhancing test coverage of the application to ensure that all critical functionality is 100% covered by automated tests.

This incident serves as a valuable learning opportunity, reinforcing our commitment to improving our processes and preventing the recurrence of similar issues. The website is now operating smoothly, and we appreciate the understanding and patience of our users during this brief disruption.
