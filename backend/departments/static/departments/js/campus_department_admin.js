
document.addEventListener("DOMContentLoaded", function () {

    const campusSelect = document.getElementById("id_campus");
    const departmentSelect = document.getElementById("id_department");

    if (!campusSelect || !departmentSelect) {
        return;
    }

    const url = campusSelect.dataset.availableDepartmentsUrl ||
    "/admin/departments/campusdepartment/available-departments/";

    const initialCampus = campusSelect.value;
    const initialDepartment = departmentSelect.value;

    const initialDepartmentText = initialDepartment
        ? departmentSelect.options[
            departmentSelect.selectedIndex
          ].text
        : "";

    async function updateDepartments(campusChanged = false) {

        const campusId = campusSelect.value;

        departmentSelect.innerHTML = "";

        departmentSelect.add(
            new Option("---------", "")
        );

        if (!campusId) {
            departmentSelect.disabled = true;
            return;
        }

        departmentSelect.disabled = true;

        try {

            const response = await fetch(
                `${url}?campus_id=${encodeURIComponent(campusId)}`,
                {
                    headers: {
                        "X-Requested-With": "XMLHttpRequest"
                    }
                }
            );

            if (!response.ok) {
                throw new Error("Unable to load departments.");
            }

            const data = await response.json();

            data.results.forEach(function (department) {

                departmentSelect.add(
                    new Option(
                        department.text,
                        department.id
                    )
                );

            });

            // Preserve the existing department when editing
            if (
                !campusChanged &&
                campusId === initialCampus &&
                initialDepartment
            ) {

                const alreadyExists = Array.from(
                    departmentSelect.options
                ).some(option => option.value === initialDepartment);

                if (!alreadyExists) {
                    departmentSelect.add(
                        new Option(
                            initialDepartmentText,
                            initialDepartment
                        )
                    );
                }

                departmentSelect.value = initialDepartment;
            }

            departmentSelect.disabled = false;

        } catch (error) {

            console.error(error);

            departmentSelect.innerHTML = "";
            departmentSelect.add(
                new Option("Unable to load departments", "")
            );

        }
    }

    campusSelect.addEventListener("change", function () {
        updateDepartments(true);
    });

    // Load available departments when the page opens
    updateDepartments(false);

});
