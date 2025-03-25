// Function to Load Data into Table
function loadData() {
  $.get("/get_data", function (data) {
    console.log("Data received from API:", data); // Debugging

    if (!Array.isArray(data)) {
      console.error("Invalid data format:", data);
      return;
    }

    // Sort the data by ID in ascending order
    data.sort((a, b) => a.id - b.id);

    let tableContent = "";
    data.forEach((entry) => {
      tableContent += `
            <tr data-id="${entry.id}">
              <td>${entry.date || "N/A"}</td>
              <td>${entry.uge_forbrug || "N/A"}</td>
              <td>${entry.tidligere_uge_forbrug || "N/A"}</td>
              <td>${entry.data_source || "N/A"}</td>
            </tr>`;
    });

    $("#data-table").html(tableContent); // Inject sorted data into the table
  }).fail(function (xhr, status, error) {
    console.error("Error fetching data:", status, error);
  });
}
loadData();
