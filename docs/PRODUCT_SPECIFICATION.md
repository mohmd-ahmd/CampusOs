    # CampusOS
    ## Complete Product Specification & Software Requirements Document

    **Organization:** IQRA ROZA TUL ATFAL TRUST AND SCHOOL SYSTEM  
    **Product:** CampusOS  
    **Document Type:** Product Requirements Document (PRD) / Software Requirements Specification (SRS)  
    **Version:** 1.0  
    **Status:** Initial development specification  
    **Purpose:** Complete reference for designing, developing, testing and maintaining CampusOS.

    ---

    # 1. Project Overview

    ## 1.1 Introduction

    CampusOS is a centralized Human Resource and Employee Performance Management Platform designed for IQRA ROZA TUL ATFAL TRUST AND SCHOOL SYSTEM.

    The organization operates across multiple campuses. CampusOS will provide a centralized platform through which the organization can manage employee information, monitor monthly performance, configure performance evaluation criteria, conduct appraisals, manage increment recommendations and generate organizational reports.

    The platform will connect all campuses through one centralized system while maintaining appropriate campus-level access restrictions.

    The initial organizational scope is 24 campuses. However, the number of campuses must never be hardcoded. Authorized administrators must be able to add, edit, deactivate and manage campuses dynamically through the website.

    CampusOS is intended to improve:

    - Employee performance monitoring.
    - HR administration.
    - Monthly performance submissions.
    - Organizational accountability.
    - Performance evaluation and appraisal.
    - Increment recommendations.
    - Reporting and management visibility.
    - Communication between central HR and individual campuses.

    ## 1.2 Product Vision

    To create one centralized, intelligent and flexible platform that connects all campuses and provides complete workforce performance visibility.

    **Suggested tagline:**

    "One platform. Every campus. Complete workforce intelligence."

    ## 1.3 Primary Objectives

    1. Centralize employee performance records.
    2. Allow HR to configure performance measures without changing source code.
    3. Monitor monthly submissions across all campuses.
    4. Maintain historical performance records.
    5. Automate configured performance calculations.
    6. Support configurable appraisal and increment recommendations.
    7. Provide role-based and campus-based access.
    8. Generate comprehensive organizational reports.
    9. Deliver real-time dashboard updates and notifications.
    10. Preserve accountability through audit logs.

    ---

    2. Organizational Structure
    2.1 Organization
    The organization is:

    IQRA ROZA TUL ATFAL TRUST AND SCHOOL SYSTEM

    CampusOS will operate as one centralized platform for the organization.
    2.2 Campus Management
    Campus management must be dynamic.

    Main HR or an authorized administrator must be able to:
    - Create a new campus.
    - Edit campus information.
    - Activate or deactivate a campus.
    - View campus details.
    - Assign departments to campuses.
    - View campus-specific employees.
    - Monitor campus performance submissions.
    - Generate campus-specific reports.
    The system must not assume that the organization will always have 24 campuses.

    Adding a campus must not require a developer to modify the database schema or source code.

    Deactivated campuses must retain their historical employee, performance and appraisal records.
    2.3 Department Management
    The organization initially proposes the following 13 departments for CampusOS:
    1. ROZA
    2. QUAIDA
    3. HIFZ
    4. LOWER STAFF
    5. SCHOOL
    6. SCHOOL HIFZ
    7. OFFICE ASSITENT
    8. NAZIM MUL UMOR
    9. NAZIM TALEEM
    10. MOAWIN NAZIM UMOR
    11. MOAWIN NAZIM TALEEM
    12. CASHIER
    13. RECORDER
    These departments must be available as initial default department records when CampusOS is configured.

    Important: These 13 departments are not a permanent or hardcoded list. CampusOS must support dynamic department management.

    Authorized administrators must be able to:
    - Create additional departments.
    - Edit department names and details.
    - Activate or deactivate departments.
    - Assign departments to individual campuses.
    - Assign employees to departments.
    - Configure department-specific performance measures.
    - Configure department-specific submission requirements.
    - View department performance reports.
    Each campus may have its own selection of departments. Not every campus is required to have all 13 departments.

    The same department may exist at multiple campuses.

    Deactivated departments must retain their historical employee, performance and appraisal records.

    Adding, editing or deactivating a department must not require changes to application source code or database schema.
    2.4 Department-Specific Configurations
    Performance requirements may differ between departments and between campuses using the same department.

    For example:
    - HIFZ at Campus 1 may have different performance measures from HIFZ at Campus 2.
    - ROZA and QUAIDA may require different performance forms.
    - SCHOOL and SCHOOL HIFZ may have separate performance evaluation criteria.
    - Administrative departments may have completely different performance measures from teaching departments.
    A performance field configured for one department must not automatically become mandatory for every other department.

    The system must support different configurations for individual campus-department combinations wherever required.

    # 3. User Management, Roles and Permissions

    ## 3.1 Dynamic Role-Based Access Control

    CampusOS must use a dynamic Role-Based Access Control (RBAC) architecture.

    Roles must not be permanently hardcoded into the application.

    An authorized administrator must be able to create and manage roles directly through the website.

    Examples of possible roles:

    - Main HR
    - Campus HR
    - CEO
    - Regional Manager
    - Performance Manager
    - Auditor
    - Finance Viewer

    These are examples, not a fixed list of roles.

    ## 3.2 Role Management

    The role management interface must support:

    - Creating roles.
    - Editing role names.
    - Adding descriptions.
    - Assigning permissions.
    - Removing permissions.
    - Activating and deactivating roles.
    - Viewing users assigned to a role.

    A role can contain any appropriate combination of available permissions.

    ## 3.3 Dynamic Permission Management

    Permissions define the actions a user is allowed to perform.

    Permissions must be defined as individual system capabilities.

    Examples:

    **Employee permissions**
    - View employees.
    - Create employees.
    - Edit employees.
    - Deactivate employees.
    - View employee history.

    **Campus permissions**
    - View campuses.
    - Create campuses.
    - Edit campuses.
    - Deactivate campuses.

    **Performance permissions**
    - View current performance.
    - Enter performance.
    - Edit performance.
    - View historical performance.
    - Edit historical performance.
    - Approve performance records.

    **Appraisal permissions**
    - View appraisal results.
    - Configure appraisal rules.
    - Generate appraisal recommendations.
    - Approve appraisal results.

    **Reporting permissions**
    - View reports.
    - Generate reports.
    - Export PDF.
    - Export Excel.

    **System permissions**
    - Manage users.
    - Manage roles.
    - Manage permissions.
    - View audit logs.
    - Manage submission schedules.

    The administrator decides which roles receive which permissions.

    The application must maintain a controlled permission catalogue so that administrators assign real capabilities supported by the software rather than inventing arbitrary actions.

    ## 3.4 Multiple Roles Per User

    A single user must be allowed to have multiple roles.

    For example, a user may simultaneously have:

    - Campus HR
    - Report Manager

    The user's effective permissions are derived from their assigned roles, subject to applicable access restrictions.

    ## 3.5 User Account Management

    Authorized administrators must be able to:

    - Create user accounts.
    - Assign usernames.
    - Set initial passwords or initiate secure password setup.
    - Assign one or more roles.
    - Assign campus or organizational scope.
    - Activate or deactivate accounts.
    - Reset passwords through a secure process.
    - Review user activity.

    Passwords must never be stored in plain text.

    Django's secure password hashing facilities must be used.

    ## 3.6 Campus-Level Access Restrictions

    Permissions and data scope are separate concepts.

    Having permission to view employees does not automatically grant access to every campus.

    For example:

    - User A may have Campus HR permissions for Campus 1.
    - User B may have Campus HR permissions for Campus 5.
    - User C may have organization-wide read permissions.

    The backend must enforce both permission and data scope.

    ## 3.7 Initial Role Examples

    The following are recommended initial role configurations. They must be created as database records, not permanently hardcoded role types.

    ### Main HR

    Typical responsibilities:

    - Organization-wide HR administration.
    - Campus and department management.
    - Employee creation and management.
    - Performance field configuration.
    - Formula configuration.
    - Submission schedule management.
    - Historical performance management.
    - Salary-scale and appraisal configuration.
    - Report generation.
    - User and role administration.

    ### Sub HR / Campus HR

    Typical responsibilities:

    - Access limited to assigned campus.
    - Search employees by Employee ID.
    - Edit existing employee information.
    - Enter monthly performance during authorized submission windows.
    - View campus-specific reports.
    - View salary-related information only if the assigned permissions allow it.

    Restrictions:

    - Cannot create or remove employees.
    - Cannot edit historical performance.
    - Cannot view historical performance numbers.
    - Cannot enter monthly performance outside authorized windows.

    ### CEO

    Typical responsibilities:

    - Organization-wide executive dashboard.
    - Read-only organizational information.
    - Performance summaries.
    - Appraisal and increment recommendation summaries.
    - Organizational reports.
    - Historical performance visibility where authorized.

    Restrictions:

    - Cannot modify records.
    - Cannot modify settings.
    - Cannot manage users or roles.
    - Cannot change performance configurations.

    These initial roles can be modified through the role-management interface.

    ---

    # 4. Employee Management

    ## 4.1 Employee Records

    Each employee must have a unique Employee ID.

    Employee records should include configurable or standard information such as:

    - Employee ID.
    - Employee name.
    - Contact information.
    - Campus.
    - Department.
    - Designation.
    - Employment status.
    - Joining date.
    - Relevant organizational information.

    The exact employee information form will be finalized during implementation.

    ## 4.2 Employee Creation

    Only users with the appropriate employee-creation permission may create employees.

    During employee creation, the authorized administrator selects:

    1. Campus.
    2. Department.
    3. Employee information.

    Employee IDs must remain unique and stable.

    ## 4.3 Employee Editing

    Authorized HR users can edit existing employee information.

    Sub HR may edit existing employee information within their assigned campus but cannot create or remove employees.

    ## 4.4 Employee Deactivation

    Employees must be deactivated rather than permanently deleted when they leave the organization or become inactive.

    Deactivation must preserve:

    - Employee information.
    - Previous campus assignments.
    - Department history.
    - Performance records.
    - Appraisal history.

    Inactive employees must not automatically appear in new monthly submission requirements.

    ## 4.5 Employee Transfers

    The system must support employee transfers between campuses and departments.

    For example:

    An employee transfers from Campus 1 to Campus 4.

    The system must preserve:

    - Previous campus.
    - Previous department.
    - New campus.
    - New department.
    - Transfer effective date.
    - Historical performance.

    Historical performance records must remain associated with the employee and their original applicable organizational assignment.

    ---

    # 5. Dynamic Performance Management

    This is one of the core modules of CampusOS.

    ## 5.1 Configurable Performance Fields

    Main HR must be able to create performance fields through the website.

    Performance measures must not be hardcoded into the source code.

    For example, one department may require:

    - Monthly attendance.
    - Student performance.
    - Syllabus completion.
    - Teaching quality.
    - Administrative responsibilities.

    Another department may require completely different measures.

    ## 5.2 Performance Field Configuration

    The field builder should support configuration such as:

    - Field name.
    - Description.
    - Associated department.
    - Associated campus or campus group, where applicable.
    - Data type.
    - Input format.
    - Minimum value.
    - Maximum value.
    - Required or optional status.
    - Display order.
    - Active or inactive status.
    - Effective date.
    - Validation rules.

    Supported field types may include:

    - Integer.
    - Decimal.
    - Percentage.
    - Text.
    - Boolean.
    - Date.
    - Selection/dropdown.

    The final supported types will be established during implementation.

    ## 5.3 Dynamic Performance Forms

    When a Sub HR opens an employee's performance form, CampusOS must load the performance fields configured for that employee's department and applicable campus.

    The form must adapt automatically.

    Adding a new performance field must not require creating a new database column or changing application source code.

    ## 5.4 Performance Records

    Every employee's monthly performance must be stored as a separate historical record.

    The system must never overwrite a previous month's performance when a new month's submission is made.

    Records must preserve the applicable performance-field and formula versions.

    ## 5.5 Performance Validation

    The system must validate:

    - Required fields.
    - Data types.
    - Minimum and maximum values.
    - Submission deadlines.
    - Employee eligibility.
    - Campus and department authorization.
    - Duplicate submissions.

    Missing performance data must not silently be treated as zero.

    Missing data must be identified as incomplete or handled through an explicitly configured business rule.

    ---

    # 6. Monthly Performance Submission System

    ## 6.1 Submission Windows

    Main HR must be able to configure monthly submission windows.

    A submission window must have:

    - Opening date and time.
    - Closing date and time.
    - Applicable year and month.
    - Applicable campuses or departments, where configured.
    - Active status.

    Pakistan Standard Time (Asia/Karachi) must be used for displaying and interpreting organizational deadlines.

    The backend must enforce the actual submission deadline.

    ## 6.2 Sub HR Submission Restrictions

    Sub HR can enter monthly performance only during the authorized submission window.

    After the closing deadline:

    - Submissions must be locked.
    - Sub HR must not be able to modify the closed month's records.
    - Main HR may edit historical records if authorized.

    The backend must enforce these restrictions even if someone attempts to submit data through a direct API request.

    ## 6.3 Submission Countdown

    The dashboard should display:

    - Time remaining until the current submission window closes.
    - When the window is closed, time remaining until the next opening.
    - Current submission status.

    The countdown must use server-synchronized deadlines rather than relying solely on the user's computer clock.

    ## 6.4 Campus Submission Status

    Campus submission status is calculated using required active employees.

    Three primary statuses are required:

    **Not Submitted**
    - Zero required employees have submitted their performance.

    **In Progress**
    - Some required employees have submitted.
    - Other required employees are still pending.

    **Submitted / Completed**
    - All required employees have submitted their required performance.

    Inactive employees and employees not required to submit must be excluded from the denominator.

    ## 6.5 Pending Employee Details

    When Main HR clicks an In Progress campus, the system must display pending employees.

    The list should contain:

    - Employee name.
    - Employee ID.
    - Campus.
    - Department.
    - Submission status.

    This will help HR identify exactly which employees have not yet been submitted.

    ## 6.6 Department-Wise Monitoring

    Main HR must be able to inspect submission progress by:

    - Campus.
    - Department.
    - Month.
    - Year.
    - Employee.

    Sub HR must only see information permitted within their assigned campus and permissions.

    Historical numeric performance values remain hidden from Sub HR unless the applicable policy is explicitly changed.

    ## 6.7 Department-Campus Holiday Configuration

    Main HR must be able to mark one or more months as holidays for a selected department and campus.

    For example:

    - Campus 1 — Hifz department — July marked as a holiday.
    - Campus 2 — Hifz department — July remains an active performance month.

    The holiday applies only to that department-campus combination in the relevant appraisal year.

    It must not automatically make the same department's month a holiday at every campus.

    Holiday exclusions must be reflected in submission requirements and completion calculations.

    ---

    # 7. Performance Calculation Engine

    ## 7.1 Dynamic Formulas

    Main HR must be able to configure formulas through the website.

    The system must support different aggregation methods according to the metric's meaning.

    Examples include:

    - SUM.
    - AVERAGE.
    - Annual completion percentage.
    - Latest value.
    - Count.
    - Weighted score.

    ## 7.2 Formula Configuration

    Formula configurations may include:

    - Formula name.
    - Description.
    - Applicable performance fields.
    - Calculation method.
    - Weight.
    - Thresholds.
    - Effective date.
    - Version.
    - Active status.

    ## 7.3 Formula Safety

    Formulas must be processed through a restricted and validated expression engine.

    The application must never execute arbitrary Python or JavaScript supplied by a user.

    ## 7.4 Missing Data

    Missing monthly records must be treated according to an explicitly configured policy.

    The system must not silently interpret missing information as zero.

    An annual calculation may be marked incomplete until the required records exist.

    ## 7.5 Historical Calculation Integrity

    When a formula is changed, previously finalized performance and appraisal results must not silently change.

    Historical records must retain the formula version used when they were calculated.

    ---

    # 8. Appraisal and Increment Recommendations

    ## 8.1 Purpose

    CampusOS will support performance-based appraisal and increment recommendations.

    It is not intended to replace the organization's existing payroll software.

    ## 8.2 Salary and Payroll Scope

    The organization already uses separate software for salary processing.

    CampusOS must not become a payroll-processing application.

    It must not implement:

    - Salary payment processing.
    - Payslip generation.
    - Payroll deductions.
    - Payroll disbursement.
    - Monthly salary calculation.
    - Payroll accounting.

    CampusOS will focus on performance appraisal and approved increment recommendations.

    ## 8.3 Configurable Grades and Distinctions

    Main HR must be able to configure appraisal grades and distinctions.

    For example:

    - Grade A.
    - Grade B.
    - Grade C.

    These are examples only.

    Grade names, score ranges, thresholds and applicable rules must be configurable.

    ## 8.4 Appraisal Configuration

    The system must support configuration of:

    - Appraisal year.
    - Applicable departments.
    - Performance formula.
    - Grade thresholds.
    - Distinction rules.
    - Increment percentage rules.
    - Eligibility requirements.
    - Approval status.

    ## 8.5 Increment Recommendations

    The appraisal engine will determine the applicable increment recommendation based on the configured performance and appraisal rules.

    The system should preserve:

    - Employee ID.
    - Appraisal year.
    - Final performance score.
    - Grade.
    - Distinction.
    - Recommended increment percentage.
    - Applied configuration version.
    - Approval status.
    - Approval date.

    Monetary salary calculations and payroll processing are outside the scope of CampusOS.

    ## 8.6 Historical Appraisal Preservation

    Once an appraisal is finalized, later changes to grades, thresholds or increment rules must not alter that historical result.

    Each appraisal must retain the configuration version used at the time.

    ## 8.7 Payroll System Handoff

    CampusOS should be capable of generating an approved increment recommendation report or export for transfer to the existing payroll system.

    The exact integration method will be finalized later.

    ---

    # 9. Reporting Centre

    CampusOS must include a centralized Reporting Centre.

    ## 9.1 Initial Required Reports

    ### Report 1: All-Campus Monthly Submission Status

    Displays the monthly performance submission status of all campuses.

    ### Report 2: Department-Wise Pending Report

    Displays departments and employees whose required submissions are pending.

    ### Report 3: Individual Employee Report

    Displays an employee's performance information.

    Must support English and Urdu.

    ### Report 4: Campus-Wise Department Report

    Displays department-level performance and submission information for a selected campus.

    ### Report 5: Appraisal Report

    Displays finalized appraisal results, grades, distinctions and increment recommendations.

    Additional report formats will be defined using the organization's actual reporting samples.

    ## 9.2 Report Filters

    Reports should support filters such as:

    - Campus.
    - Department.
    - Employee ID.
    - Employee name.
    - Month.
    - Year.
    - Submission status.
    - Appraisal year.
    - Grade.
    - Distinction.
    - Language.

    ## 9.3 Export Formats

    Reports must support:

    - PDF.
    - Excel.

    ## 9.4 Urdu Reporting

    Urdu PDF exports must support proper right-to-left text rendering and suitable Unicode fonts.

    Text direction, alignment, tables and page layout must be tested with actual Urdu content.

    ## 9.5 Historical Integrity

    Appraisal reports must use approved appraisal records rather than independently recalculating historical results.

    ---

    # 10. Dashboard and Analytics

    CampusOS will provide different dashboards according to user permissions and data scope.

    ## 10.1 Main HR Dashboard

    The Main HR dashboard should provide:

    - Total active campuses.
    - Total active departments.
    - Total active employees.
    - Monthly submission progress.
    - Completed campuses.
    - In-progress campuses.
    - Pending campuses.
    - Department-wise statistics.
    - Performance trends.
    - Appraisal summaries.
    - Notifications.

    The dashboard must allow authorized users to navigate from organizational summaries into detailed campus and department information.

    ## 10.2 Sub HR Dashboard

    The Sub HR dashboard should display:

    - Assigned campus information.
    - Active employees.
    - Department information.
    - Current submission window.
    - Submission countdown.
    - Submission progress.
    - Pending employees.
    - Relevant campus reports.

    The dashboard must not expose unauthorized historical numeric performance information.

    ## 10.3 CEO Dashboard

    The CEO dashboard must be read-only.

    It should provide organization-wide executive visibility, including:

    - Organizational performance summaries.
    - Campus comparisons.
    - Department performance.
    - Submission completion.
    - Historical performance.
    - Appraisal summaries.
    - Approved increment recommendations.
    - Reports.

    The CEO must not be able to modify records or settings.

    ## 10.4 Analytics and Visualization

    The platform should support:

    - Interactive charts.
    - Performance trends.
    - Campus comparisons.
    - Department comparisons.
    - Completion percentages.
    - Historical performance analysis.

    A selective 3D campus network visualization may be used on the executive dashboard.

    3D visualizations must not make routine HR tasks slow or difficult.

    ---

    # 11. Real-Time Updates and Notifications

    ## 11.1 Real-Time Requirement

    CampusOS must update relevant information without requiring users to manually refresh the page.

    ## 11.2 Real-Time Examples

    When an authorized user:

    - Adds an employee, relevant employee lists update automatically.
    - Submits monthly performance, submission monitoring updates.
    - Completes a campus submission, dashboard statistics update.
    - Changes a role's permissions, affected user access is synchronized.
    - Changes a submission schedule, relevant dashboards reflect the new schedule.
    - Generates a notification-triggering event, authorized users receive a live notification.

    ## 11.3 Notification System

    Notifications may include:

    - Submission window opening.
    - Submission deadline approaching.
    - Submission deadline passed.
    - Pending employee submissions.
    - Campus submission completed.
    - Employee changes.
    - Role or permission changes.
    - Appraisal approval.

    Users should only receive notifications relevant to their roles and organizational scope.

    ## 11.4 Real-Time Technology

    Proposed technologies:

    - Django Channels.
    - WebSockets.
    - Redis.
    - TanStack Query.

    Real-time delivery must include authentication, authorization and campus-level event restrictions.

    ## 11.5 Reconnection and Synchronization

    If a user's internet connection disconnects:

    - The application should attempt to reconnect.
    - It should synchronize relevant data after reconnection.
    - It must not assume that missed events were received.
    - The database remains the authoritative source of saved information.

    ---

    # 12. Audit Logs and Accountability

    Important administrative and business actions must be recorded.

    Examples:

    - Employee created.
    - Employee edited.
    - Employee deactivated.
    - Employee transferred.
    - Role created.
    - Permission assigned or removed.
    - User account changed.
    - Performance submitted.
    - Historical performance edited.
    - Appraisal finalized.
    - Submission window changed.

    Audit records should preserve:

    - User who performed the action.
    - Action type.
    - Affected record.
    - Date and time.
    - Relevant previous and new values, where appropriate.

    Ordinary users must not be able to alter or delete audit history.

    Access to audit logs must itself be permission-controlled.

    ---

    # 13. User Interface and Design Requirements

    ## 13.1 Design Direction

    CampusOS should have a premium, modern enterprise interface.

    Design decisions:

    - Hybrid light and dark themes.
    - Premium light theme as the default.
    - Optional dark theme.
    - Indigo/violet accent colors.
    - Neutral surfaces.
    - Inter typography.
    - Minimal visual personality.
    - Rich but purposeful animation.
    - Responsive layouts.

    ## 13.2 Dashboard Design

    The dashboard will use a hybrid approach:

    - Clean information cards.
    - Interactive analytics.
    - Selective 3D visualization.
    - Animated statistics.
    - Smooth transitions.
    - Interactive charts.

    ## 13.3 User Experience

    The interface should provide:

    - Clear navigation.
    - Search and filtering.
    - Fast forms.
    - Helpful validation.
    - Confirmation for important actions.
    - Loading skeletons.
    - Success and error feedback.
    - Accessible controls.
    - Responsive layouts.

    Performance data-entry forms should prioritize speed and clarity over decorative animation.

    ## 13.4 Responsive Design

    The website must work on:

    - Desktop.
    - Laptop.
    - Tablet.
    - Mobile.

    ---

    # 14. Technical Architecture

    ## 14.1 Architecture Style

    CampusOS should initially use a modular monolithic architecture.

    Microservices are not required for the first development phase.

    This will keep the system easier to develop, test, maintain and deploy.

    ## 14.2 Frontend

    Proposed stack:

    - Next.js App Router.
    - React.
    - TypeScript with strict mode.
    - Tailwind CSS.
    - shadcn/ui.
    - Motion for React.
    - React Three Fiber.
    - Three.js.
    - Apache ECharts.
    - TanStack Query.
    - React Hook Form.
    - Zod.

    ## 14.3 Backend

    Proposed stack:

    - Python.
    - Django.
    - Django REST Framework.
    - Django Channels.

    ## 14.4 Database

    PostgreSQL will be the primary database.

    The system should use relational models and constraints for organizational, employee, performance and appraisal data.

    Dynamic performance definitions should be stored separately from performance values.

    The system must not create a new physical database column every time an administrator creates a performance field.

    ## 14.5 Real-Time Infrastructure

    - Redis.
    - Django Channels.
    - WebSockets.
    - Background processing where required.

    ## 14.6 Deployment

    Proposed infrastructure:

    - Docker.
    - Docker Compose for development.
    - PostgreSQL.
    - Redis.
    - Production application server.
    - Secure HTTPS deployment.
    - Automated backups.

    Deployment provider and hosting specifications will be selected later.

    ---

    # 15. Proposed Database Model Structure

    The following is a preliminary logical model inventory. Exact fields, relationships and constraints will be finalized during database design.

    ## 15.1 Accounts

    - User
    - Role
    - Permission
    - RolePermission
    - UserRoleAssignment
    - UserCampusAssignment

    ## 15.2 Organizations

    - Campus
    - Department
    - Employee
    - EmployeeHistory

    ## 15.3 Performance

    - PerformanceField
    - PerformanceFieldVersion
    - PerformanceRecord
    - PerformanceValue
    - SubmissionWindow
    - DepartmentCampusHoliday
    - PerformanceFormula
    - FormulaVersion

    ## 15.4 Appraisal

    - AppraisalYear
    - AppraisalConfiguration
    - AppraisalGrade
    - IncrementRule
    - AppraisalResult
    - AppraisalApproval

    ## 15.5 System

    - AuditLog
    - Notification
    - UserNotification
    - SystemSetting

    The exact data model must be normalized appropriately, with foreign keys, indexes, uniqueness constraints and appropriate deletion policies.

    Historical business records must not be accidentally deleted when related organizational records are deactivated.

    ---

    # 16. Security Requirements

    Security must be implemented at the backend and database layers.

    Requirements:

    1. Secure authentication.
    2. Password hashing.
    3. Permission enforcement on APIs.
    4. Campus-level data restrictions.
    5. Secure session or token management.
    6. Input validation.
    7. Protection against unauthorized record modification.
    8. CSRF and CORS configuration where applicable.
    9. HTTPS in production.
    10. Secret management through environment variables.
    11. Audit logging.
    12. Database backups.
    13. Secure WebSocket authentication.
    14. Protection against unauthorized real-time event subscriptions.

    The frontend must never be considered the security boundary.

    Hiding a button is not sufficient to protect an operation.

    ---

    # 17. Data Integrity and Historical Records

    Historical preservation is a major requirement.

    The system must preserve:

    - Employee history.
    - Campus transfers.
    - Department transfers.
    - Monthly performance records.
    - Performance field versions.
    - Formula versions.
    - Appraisal configurations.
    - Finalized appraisal results.
    - Approved increment recommendations.

    Important records should be deactivated, archived or versioned rather than physically deleted.

    Database transactions and constraints must protect important operations against partial or duplicate updates.

    ---

    # 18. Business Rules and Special Cases

    The following rules must be respected throughout development:

    1. Campus count must be dynamic.
    2. Department count must be dynamic.
    3. Employee IDs must be unique.
    4. Main HR or authorized administrators control employee creation and deactivation.
    5. Sub HR cannot create or remove employees.
    6. Sub HR cannot edit historical performance.
    7. Sub HR cannot enter performance outside the authorized submission window.
    8. Historical performance records must be preserved.
    9. Monthly submission completion must use eligible active employees.
    10. Inactive employees must not be counted as pending.
    11. Missing data must not silently become zero.
    12. Department-campus holiday settings must be independent.
    13. Performance fields must be configurable.
    14. Formula changes must not silently rewrite historical results.
    15. Appraisal rules must be versioned.
    16. CEO access must remain read-only.
    17. Roles and role permissions must be dynamically managed.
    18. A user may have multiple roles.
    19. Campus scope must be enforced independently of role permissions.
    20. Payroll processing is outside CampusOS scope.

    ---

    # 19. Development Roadmap

    ## Phase 1 — Project Foundation

    - GitHub repository.
    - Backend environment.
    - Django project.
    - PostgreSQL connection.
    - Environment configuration.
    - Custom user model.
    - Dynamic RBAC.
    - Initial migrations.
    - API foundation.

    ## Phase 2 — Organization Management

    - Campus management.
    - Department management.
    - Employee management.
    - Employee history.
    - Transfers.
    - Deactivation.

    ## Phase 3 — Frontend Foundation

    - Next.js setup.
    - Design system.
    - Login.
    - Application layout.
    - Navigation.
    - Theme system.
    - Dashboard structure.

    ## Phase 4 — User and Permission Management

    - User creation.
    - Role creation.
    - Permission assignment.
    - Multiple roles.
    - Campus assignment.
    - Account management.

    ## Phase 5 — Performance Management

    - Dynamic performance field builder.
    - Department-specific forms.
    - Performance data storage.
    - Validation.
    - Historical records.

    ## Phase 6 — Submission Management

    - Submission schedules.
    - Countdown.
    - Monthly entry.
    - Campus completion monitoring.
    - Pending employee lists.
    - Department-campus holidays.
    - Submission locking.

    ## Phase 7 — Calculation Engine

    - Formula builder.
    - Aggregation.
    - Missing-data handling.
    - Version management.
    - Performance scoring.

    ## Phase 8 — Appraisal

    - Appraisal years.
    - Configurable grades.
    - Configurable thresholds.
    - Increment recommendations.
    - Approval workflows.
    - Historical appraisal preservation.

    ## Phase 9 — Real-Time Features

    - WebSockets.
    - Redis.
    - Live dashboard.
    - Notifications.
    - Automatic synchronization.
    - Reconnection handling.

    ## Phase 10 — Reporting

    - Monthly status reports.
    - Pending reports.
    - Employee reports.
    - Department reports.
    - Appraisal reports.
    - PDF exports.
    - Excel exports.
    - Urdu RTL support.

    ## Phase 11 — Testing and Deployment

    - Functional testing.
    - Permission testing.
    - Campus isolation testing.
    - Calculation testing.
    - Security testing.
    - Performance testing.
    - Backup and restore testing.
    - Production deployment.

    ---

    # 20. Proposed Repository Structure

    ```text
    CampusOS/
    │
    ├── docs/
    │   ├── README.md
    │   ├── PRODUCT_SPECIFICATION.md
    │   ├── DATABASE_DESIGN.md
    │   ├── BUSINESS_RULES.md
    │   ├── API_DOCUMENTATION.md
    │   ├── DESIGN_SYSTEM.md
    │   └── DEVELOPMENT_PROGRESS.md
    │
    ├── frontend/
    │   └── Next.js application
    │
    ├── backend/
    │   ├── campus_accounts/
    │   ├── organizations/
    │   ├── performance/
    │   ├── appraisals/
    │   ├── reports/
    │   ├── notifications/
    │   ├── config/
    │   ├── manage.py
    │   └── .env
    │
    ├── docker-compose.yml
    ├── .gitignore
    └── README.md
    ```

    This structure is a proposed target. Existing `accounts` and `organizations` folders should be preserved and used unless a deliberate migration plan is approved.

    The `.env` file must never be committed to GitHub.

    ---

    # 21. Testing Requirements

    Before production, CampusOS must be tested for:

    ## Functional Testing
    - User login.
    - Role creation.
    - Permission assignment.
    - Employee management.
    - Campus management.
    - Performance submission.
    - Appraisal calculations.
    - Report generation.

    ## Authorization Testing
    - Unauthorized users cannot access restricted APIs.
    - Sub HR cannot access other campuses.
    - Sub HR cannot modify historical records.
    - CEO cannot modify records.
    - Multiple roles combine permissions correctly.
    - Campus scope remains enforced.

    ## Data Integrity Testing
    - Employee transfers preserve history.
    - Deactivated employees remain in historical reports.
    - Performance field changes preserve old records.
    - Formula changes do not rewrite finalized appraisals.
    - Duplicate submissions are prevented.

    ## Real-Time Testing
    - Dashboard updates after submissions.
    - Notifications reach authorized users.
    - Disconnected clients resynchronize.
    - Unauthorized users cannot subscribe to restricted events.

    ## Reporting Testing
    - PDF layout.
    - Excel exports.
    - Urdu RTL rendering.
    - Historical calculation consistency.

    ---

    # 22. Requirements Still Requiring Final Confirmation

    The following details are not yet fully specified and must be finalized before implementing their respective modules.

    1. **Employee form:** Exact personal, employment and organizational fields.
    2. **Performance field types:** Final supported input types and validation rules.
    3. **Appraisal frequency:** Monthly, annual or both.
    4. **Appraisal eligibility:** Minimum required months, missing records and employee eligibility rules.
    5. **Increment rules:** Exact percentage brackets and approval process.
    6. **Appraisal approval workflow:** Who reviews, approves or rejects recommendations.
    7. **Report templates:** Actual organization-provided PDF/Excel formats.
    8. **Urdu reports:** Exact fonts, terminology and layouts.
    9. **Payroll handoff:** Manual export, spreadsheet or future API integration.
    10. **Authentication policy:** Password reset, session duration and optional multi-factor authentication.
    11. **User role administration:** Which administrator can create or modify the highest-privilege roles.
    12. **Historical visibility:** Final historical status and numeric-data visibility policy for each role.

    These decisions must be documented as they are finalized.

    ---

    # 23. Definition of a Successful CampusOS

    CampusOS will be considered functionally successful when:

    - All campuses can be managed from one platform.
    - Departments can be configured dynamically.
    - Employees have stable identities and preserved history.
    - Administrators can create roles and assign permissions through the website.
    - Users can securely log in and receive appropriate access.
    - Performance fields and formulas can be configured without code changes.
    - Monthly submissions are monitored and enforced.
    - Historical performance is preserved.
    - Appraisal results and increment recommendations are calculated using approved configurations.
    - Management can generate reliable reports.
    - Real-time updates work without manual page refreshes.
    - All sensitive operations are protected by backend permissions.
    - The platform is reliable, responsive and maintainable.

    ---

    # 24. Final Product Statement

    CampusOS is a centralized, configurable and real-time employee performance management platform for IQRA ROZA TUL ATFAL TRUST AND SCHOOL SYSTEM.

    It brings organizational management, employee records, dynamic performance evaluation, monthly submission monitoring, appraisal recommendations, analytics and reporting together in one secure platform.

    Its architecture must remain flexible enough to support organizational growth, new campuses, new departments, new roles, changing performance requirements and evolving appraisal policies without repeatedly redesigning the application.

    **Core principle: CampusOS must be configurable through its website wherever business rules are expected to change, while maintaining secure, controlled and auditable system behavior.**
