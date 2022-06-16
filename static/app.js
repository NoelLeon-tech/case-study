const ronin = document.querySelector('#update-ronin')
const firstName = document.querySelector('#update-first')
const lastName = document.querySelector('#update-last')
const scholarShare = document.querySelector('#update-scholar_share')
const managerShare = document.querySelector('#update-manager_share')
const totalSlp = document.querySelector('#update-total_slp')
const deleteRonin = document.querySelector('#delete-ronin')

const table = document.querySelector('#table')
const rows = [...table.rows]

for (const [i, row] of rows.entries()) {
    if (i !== 0) {
        row.addEventListener('click', () => {
            ronin.value = row.cells[0].innerHTML
            firstName.value = row.cells[1].innerHTML
            lastName.value = row.cells[2].innerHTML
            scholarShare.value = row.cells[3].innerHTML
            managerShare.value = row.cells[4].innerHTML
            totalSlp.value = row.cells[5].innerHTML

            deleteRonin.value = row.cells[0].innerHTML
        })
    }
}