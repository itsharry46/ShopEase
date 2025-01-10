$(document).ready(function () {
  $("#category_status").on("change", function () {
    product_listing_filters("category_status", "category-status-label");
  });

  $("#product_category").on("change", function () {
    product_listing_filters("product_category", "product-category-label");
  });

  $("#product_stock_status").on("change", function () {
    product_listing_filters("product_stock_status", "product-stock-status-label");
  });
});

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

// Product Filters
const searchProductInputBox = document.getElementById("search_product");
searchProductInputBox.addEventListener("keydown", function (event) {
  if (event.key === "Enter" && searchProductInputBox.value != "") {
    product_listing_filter_fetch();
  }
});

function product_listing_filters(filter_name, label_name) {
  const selectedValue = document.getElementById(filter_name).value;
  const labelElement = document.getElementById(label_name);

  if (selectedValue !== "None") {
    labelElement.removeAttribute("hidden");
    labelElement.classList.add("floating-label");
  } else {
    labelElement.setAttribute("hidden", true);
    labelElement.classList.remove("floating-label");
  }

  product_listing_filter_fetch();
}

const productListingTableBody = document.getElementById("product-listing-table");
const productListingTableInfo = document.getElementById("product-listing-info");
const productListingTablePagination = document.getElementById("product-listing-pagination");
async function product_listing_filter_fetch(page = 1) {
  params = {
    page: page,
    category_status: document.getElementById("category_status").value,
    product_category: document.getElementById("product_category").value,
    product_stock_status: document.getElementById("product_stock_status").value,
    search_product: document.getElementById("search_product").value,
  };
  let query_params = new URLSearchParams(params).toString();
  query_params = "query_params=" + btoa(query_params);

  fetch(`inventory_view_products_fetch?${query_params}`, {
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
      const product_table_item = data.product_list;
      productListingTableBody.innerHTML = "";
      product_table_item.forEach((product_table_item) => {
        const row = `
                  <tr>
                    <td>
                      <div class="d-flex justify-content-start align-items-center product-name">
                        <div class="d-flex flex-column">
                          <h6 class="text-nowrap mb-0">${product_table_item.product_name}</h6>
                          <small class="text-truncate d-none d-sm-block">${product_table_item.product_description}</small>
                        </div>
                      </div>
                    </td>
                    <td>
                      <span class="text-truncate d-flex align-items-center text-heading">
                        <span class="w-px-30 h-px-30 rounded-circle d-flex justify-content-center align-items-center bg-label-success me-4">
                          <i class="bx bx-walk bx-sm"></i>
                        </span>${product_table_item.product_category_name}
                      </span>
                    </td>
                    <td>
                      <span>${product_table_item.product_sku}</span>
                    </td>
                    <td>
                      <span>${product_table_item.product_price}</span>
                    </td>
                    <td>
                      <span>${product_table_item.product_quantity}</span>
                    </td>
                    <td>
                      <span class="badge bg-label-danger" text-capitalized="">${product_table_item.product_status}</span>
                    </td>
                    <td>
                      <div class="d-inline-block text-nowrap">
                        <button class="btn btn-icon">
                          <i class="bx bx-edit bx-md"></i>
                        </button>
                        <button class="btn btn-icon dropdown-toggle hide-arrow" data-bs-toggle="dropdown">
                          <i class="bx bx-dots-vertical-rounded bx-md"></i>
                        </button>
                        <div class="dropdown-menu dropdown-menu-end m-0">
                          <a href="javascript:0;" class="dropdown-item">View</a>
                          <a href="javascript:0;" class="dropdown-item">Suspend</a>
                        </div>
                      </div>
                    </td>
                  </tr>
                `;
        productListingTableBody.innerHTML += row;
      });

      // Table Info
      const product_table_info = data.product_obj;
      productListingTableInfo.textContent = `Displaying ${product_table_info.start_index} to ${product_table_info.end_index} of ${data.product_count} entries`;

      productListingTablePagination.innerHTML = "";
      // Previous Button
      if (product_table_info.has_previous) {
        productListingTablePagination.innerHTML += `
          <li class="paginate_button page-item previous">
            <a href="#" onclick="product_listing_filter_fetch(${product_table_info.previous_page_number})" tabindex="-1" class="page-link">
              <i class="bx bx-chevron-left bx-18px"></i>
            </a>
          </li>
        `;
      } else {
        productListingTablePagination.innerHTML += `
          <li class="paginate_button page-item previous disabled">
            <a class="page-link">
              <i class="bx bx-chevron-left bx-18px"></i>
            </a>
          </li>
        `;
      }

      // Page numbers
      for (let i = 1; i <= product_table_info.pagination_count; i++) {
        productListingTablePagination.innerHTML += `
          <li class="paginate_button page-item ${i === product_table_info.current_page ? "active" : ""}">
              <a href="#" onclick="product_listing_filter_fetch(${i});" tabindex="0" class="page-link">${i}</a>
          </li>
        `;
      }

      // Next button
      if (product_table_info.has_next) {
        productListingTablePagination.innerHTML += `
          <li class="paginate_button page-item next">
              <a href="#" onclick="product_listing_filter_fetch(${product_table_info.next_page_number})" tabomdex="-1" class="page-link">
                  <i class="bx bx-chevron-right bx-18px"></i>
              </a>
          </li>
        `;
      } else {
        productListingTablePagination.innerHTML += `
          <li class="paginate_button page-item next disabled">
              <a class="page-link">
                  <i class="bx bx-chevron-right bx-18px"></i>
              </a>
          </li>
        `;
      }
    })
    .catch((errors) => {
      console.log(errors);
    });
}
document.addEventListener("DOMContentLoaded", product_listing_filter_fetch());

// Add Products
const addProducts = document.getElementById("add_products");
addProducts.addEventListener("click", function () {
  window.location.href = "add_products";
});

// Export Products
const exportProducts = document.getElementById("export_products");
exportProducts.addEventListener("click", function () {
  export_product_listing();
});
async function export_product_listing() {
  const toast_notification = document.getElementById("toastNotify");
  const toast_body = document.querySelector(".toastNotify-body");

  var fetch_data = {
    category_status: document.getElementById("category_status").value,
    product_category: document.getElementById("product_category").value,
    product_stock_status: document.getElementById("product_stock_status").value,
    search_product: document.getElementById("search_product").value,
  };

  fetch("inventory_view_products_export_fetch", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": commonGetCSRFToken(), // Include CSRF token
    },
    body: JSON.stringify(fetch_data),
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
      toast_body.innerHTML = data.res_message;
      toast_notification.classList.add("bg-primary");

      var toast = new bootstrap.Toast(toast_notification);
      toast.show();

      setTimeout(function () {
        const file_url = "/static/assets/exports/" + data.res_fileName + ".csv";
        commonDownloadFile(file_url);
      }, 2000);
    })
    .catch((errors) => {
      toast_body.innerHTML = errors.message;
      toast_notification.classList.add("bg-primary");

      var toast = new bootstrap.Toast(toast_notification);
      toast.show();
    });
}
