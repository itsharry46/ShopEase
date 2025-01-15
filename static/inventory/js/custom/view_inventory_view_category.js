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

  // Calling the get function to fetch the information of the selected category for Edit
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
        const clearErrors = ["category_name_error", "category_description_error", "category_status_error"];

        for (let index = 0; index < clearErrors.length; index++) {
          document.getElementById(clearErrors[index]).textContent = "";
        }

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

  // Calling the delete function to delete the specific record
  $("#Category_DataTables").on("click", ".categoryDelete-btn", function () {
    var category_id = $(this).attr("id").split("_")[1];

    const toast_notification = document.getElementById("toastNotify");
    const toast_body = document.querySelector(".toastNotify-body");

    fetch(`delete_category?category_id=${category_id}`, {
      method: "DELETE",
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
        toast_body.innerHTML = data.message;
        toast_notification.classList.add("bg-primary");

        var toast = new bootstrap.Toast(toast_notification);
        toast.show();

        setTimeout(function () {
          window.location.href = "";
        }, 2000);
      })
      .catch((errors) => {
        toast_body.innerHTML = errors.message;
        toast_notification.classList.add("bg-primary");

        var toast = new bootstrap.Toast(toast_notification);
        toast.show();
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

const searchCategoryInputBox = document.getElementById("search_category");
searchCategoryInputBox.addEventListener("keydown", function (event) {
  if (event.key === "Enter") {
    category_listing_fetch();
  }
});

const categoryListingTableBody = document.getElementById("category-listing-table");
async function category_listing_fetch() {
  params = {
    search_category: document.getElementById("search_category").value,
  };
  let query_params = new URLSearchParams(params).toString();
  query_params = "query_params=" + btoa(query_params);

  fetch(`inventory_view_category_fetch?${query_params}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
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
      // Table Items
      const category_table_item = data.category_list;
      categoryListingTableBody.innerHTML = "";
      category_table_item.forEach((category_table_item) => {
        const row = `
                    ${category_table_item.category_status == "N" ? '<tr style="background-color: rgb(255 126 126 / 20%);">' : "<tr>"}

                      <td class="  control" tabindex="0" style="display: none;"></td>
                        <td class="">
                          <div class="d-flex align-items-center">
                            <div class="d-flex flex-column justify-content-center">
                              <span class="text-heading text-wrap fw-medium">${category_table_item.category_name}</span>
                              <span class="text-truncate mb-0 d-none d-sm-block">
                              <small>${category_table_item.category_description}</small>
                              </span>
                            </div>
                          </div>
                        </td>

                        <td class="sorting_1">
                            <div class="text-sm-center">${category_table_item.category_product_count}</div>
                        </td>
              
                        <td>
                          <div class="d-flex align-items-sm-center justify-content-sm-center">
                              <button id="editCategoryItem_${
                                category_table_item.category_id
                              }" class="btn btn-icon categoryEdit-btn" data-bs-toggle="offcanvas" data-bs-target="#offcanvasEcommerceCategoryList" data-category-status="edit_mode">
                                  <i class="bx bx-edit bx-md"></i>
                              </button>
                              <button id="deleteCategoryItem_${
                                category_table_item.category_id
                              }" class="btn btn-icon dropdown-toggle hide-arrow categoryDelete-btn" ${
          category_table_item.category_status == "N" ? "disabled" : ""
        } >
                                  <i class="bx bx-trash bx-md"></i>
                              </button>
                          </div>
                        </td>

                    </tr>
                `;
        categoryListingTableBody.innerHTML += row;
      });
    })
    .catch((errors) => {
      console.log(errors);
    });
}
document.addEventListener("DOMContentLoaded", category_listing_fetch());
