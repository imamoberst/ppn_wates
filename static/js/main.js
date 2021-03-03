let rincianKeluarga = []
const clickKeluarga = document.getElementById('savekeluarga')
const tbodykeluarga = document.getElementById('tbodykeluarga')
const datakel = document.getElementById('datakel')
const jmlpenghuni = document.getElementById('jmlpenghuni')
jmlpenghuni.value = rincianKeluarga.length + 1
clickKeluarga.addEventListener('click', () => {
    const namakel = document.getElementById('namakeluarga')
    const statuskeluarga = document.getElementById('statuskeluarga')
    const keterangan = document.getElementById('keterangan')
    if (namakel.value === '') {
        alert('Nama Keluarga mohon di isi')
    } else if (statuskeluarga.value === '') {
        alert('Status Hubungan Keluarga mohon di isi')
    } else if (namakel.value !== '' && statuskeluarga.value !== '') {
        let number = rincianKeluarga.length + 1
        rincianKeluarga.push({
            "indexkeluarga": number,
            "namakeluarga": namakel.value,
            "hubungankeluarga": statuskeluarga.value,
            "keterangan": keterangan.value
        })
        tbodykeluarga.innerHTML += `<tr><td>${number}</td><td>${namakel.value}</td><td>${statuskeluarga.value}</td><td>${keterangan.value}</td><td><button type="button" class="btn btn-danger btn-sm" id="deletekel" data-namakel="${namakel.value}" data-hub="${statuskeluarga.value}" data-ket="${keterangan.value}">Delete</button></td></tr>`
        datakel.value = JSON.stringify(rincianKeluarga)
        addkeluarga.modal('hide')
        jmlpenghuni.value = rincianKeluarga.length + 1

        deletekeluarga()
    } else {
        alert('Mohon di isi dulu Nama keluarga dan Hubungan Keluarga')
    }
})

function deletekeluarga() {
    const deletekel = document.querySelectorAll('#deletekel')
    for (let i = 0; i < deletekel.length; i++) {
        deletekel[i].addEventListener('click', function () {
            const namakel = deletekel[i].dataset.namakel
            const hub = deletekel[i].dataset.hub
            const ket = deletekel[i].dataset.ket
            let newrinci = rincianKeluarga.filter(function (keluarga) {
                return keluarga.namakeluarga !== namakel
            })
            tbodykeluarga.innerHTML = ''
            rincianKeluarga = newrinci
            if (rincianKeluarga.length !== 0) {
                rincianKeluarga.forEach(function (keluarga, index) {
                    let tr = document.createElement('tr');
                    let kel = `<tr><td>${index + 1}</td><td>${keluarga.namakeluarga}</td><td>${keluarga.hubungankeluarga}</td><td>${keluarga.keterangan}</td><td><button type="button" class="btn btn-danger btn-sm" id="deletekel" data-namakel="${keluarga.namakeluarga}" data-hub="${keluarga.hubungankeluarga}" data-ket="${keluarga.keterangan}">Delete</button></td></tr>`
                    tr.innerHTML = kel
                    tbodykeluarga.appendChild(tr)
                    jmlpenghuni.value = rincianKeluarga.length + 1
                    deletekeluarga()
                })
            } else {
                jmlpenghuni.value = rincianKeluarga.length + 1
                tbodykeluarga.innerHTML = ''
            }
            datakel.value = JSON.stringify(rincianKeluarga)
        })

    }
}


