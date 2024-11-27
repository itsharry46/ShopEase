$(document).ready(function () {
  category_status_label_toggle();
  $("#category_status").on("change", function () {
    category_status_label_toggle();
  });

  $("#Category_DataTables").DataTable({
    scrollY: "74vh",
    scrollX: false,
    paging: false,
    searching: false,
    info: false,
  });

  // Calling the get function to fetch the information of the selected category
  $("#Category_DataTables").on("click", ".categoryEdit-btn", function () {
    document.getElementById("submit_update_category").style.removeProperty("display");
    document.getElementById("submit_add_category").style.setProperty("display", "none", "important");

    var category_id = $(this).attr("id").split("_")[1];
    document.getElementById("hidden_category_id").value = category_id;

    fetch(`info_update_category?category_id=${category_id}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": commonGetCSRFToken(), // Include CSRF token
      },
    })
      .then((response) => {
        if (!response.ok) {
          return response.json().then((errors) => {
            throw errors;
          });
        }
        return response.json();
      })
      .then((data) => {
        document.getElementById("category_name").value = data.category_name;
        document.getElementById("category_description").value = data.category_description;

        $("#category_status").select2("val", data.category_status);
      })
      .catch((errors) => {
        for (let key in errors) {
          if (errors.hasOwnProperty(key)) {
            document.getElementById(`${key}_error`).textContent = errors[key];
          }
        }
      });
  });
});

function category_status_label_toggle() {
  const selectedValue = $("#category_status").val();
  const labelElement = document.getElementById("category-status-label");

  if (selectedValue !== "") {
    labelElement.classList.add("floating-label");
  } else {
    labelElement.classList.remove("floating-label");
  }
}

$(function () {
  var s,
    o,
    e = $(".select2"),
    e =
      (e.length &&
        e.each(function () {
          var e = $(this);
          e.wrap('<div class="position-relative"></div>').select2({ dropdownParent: e.parent(), placeholder: e.data("placeholder") });
        }),
      $(".form-repeater"));
  e.length &&
    ((s = 2),
    (o = 1),
    e.on("submit", function (e) {
      e.preventDefault();
    }),
    e.repeater({
      show: function () {
        var a = $(this).find(".form-control, .form-select"),
          t = $(this).find(".form-label");
        a.each(function (index) {
          var r = "form-repeater-" + s + "-" + o;
          // Check if the ID already exists
          if ($("#" + r).length === 0) {
            $(a[index]).attr("id", r);
            $(t[index]).attr("for", r);
            o++;
          } else {
            // Optionally handle the case where the ID already exists
            console.warn("ID already exists: " + r);
          }
        });
        s++,
          $(this).slideDown(),
          $(".select2-container").remove(),
          $(".select2.form-select").select2({ placeholder: "Placeholder text" }),
          $(".select2-container").css("width", "100%"),
          $(".form-repeater:first .form-select").select2({ dropdownParent: $(this).parent(), placeholder: "Placeholder text" }),
          $(".position-relative .select2").each(function () {
            $(this).select2({ dropdownParent: $(this).closest(".position-relative") });
          });
      },
    }));
});

/* Custom Code Starts Here */
document.getElementById("search_category").addEventListener("keyup", function () {
  // Get the value of the search input
  const searchTerm = this.value.toLowerCase();
  const rows = document.querySelectorAll("#DataTables_Table_0 tbody tr");

  rows.forEach((row) => {
    // Get the text content of each cell in the current row
    const cells = row.getElementsByTagName("td");

    let rowVisible = false;

    // Check if any cell contains the search term
    for (let i = 0; i < cells.length; i++) {
      const cell = cells[i];
      if (cell.textContent.toLowerCase().indexOf(searchTerm) > -1) {
        rowVisible = true;
        break; // If a match is found, no need to check further
      }
    }

    // Show or hide the row based on the search term
    row.style.display = rowVisible ? "" : "none";
  });
});
