const centangJan = document.querySelector('.januari')
const centangFeb = document.querySelector('.febuari')
const centangMar = document.querySelector('.maret')
const centangApr = document.querySelector('.april')
const centangMei = document.querySelector('.mei')
const centangJun = document.querySelector('.juni')
const centangJul = document.querySelector('.juli')
const centangAug = document.querySelector('.agustus')
const centangSep = document.querySelector('.september')
const centangOct = document.querySelector('.oktober')
const centangNov = document.querySelector('.november')
const centangDes = document.querySelector('.desember')
dataiuran.forEach(function (d) {
    if ('januari' === d.bulan) {
        centangJan.removeAttribute('href')
        centangJan.classList.replace('btn-danger', 'btn-success')
        centangJan.firstElementChild.classList.replace('fa-times', 'fa-check')
        if ('verifikasi' === d.status) {
            centangJan.classList.replace('btn-success', 'btn-warning')
            centangJan.firstElementChild.classList.replace('fa-check', 'fa-exclamation')
        }
    }
    if ('febuari' === d.bulan) {
        centangFeb.removeAttribute('href')
        centangFeb.classList.replace('btn-danger', 'btn-success')
        centangFeb.firstElementChild.classList.replace('fa-times', 'fa-check')
        if ('verifikasi' === d.status) {
            centangFeb.classList.replace('btn-success', 'btn-warning')
            centangFeb.firstElementChild.classList.replace('fa-check', 'fa-exclamation')
        }
    }
    if ('maret' === d.bulan) {
        centangMar.removeAttribute('href')
        centangMar.classList.replace('btn-danger', 'btn-success')
        centangMar.firstElementChild.classList.replace('fa-times', 'fa-check')
        if ('verifikasi' === d.status) {
            centangMar.classList.replace('btn-success', 'btn-warning')
            centangMar.firstElementChild.classList.replace('fa-check', 'fa-exclamation')
        }
    }
    if ('april' === d.bulan) {
        centangApr.removeAttribute('href')
        centangApr.classList.replace('btn-danger', 'btn-success')
        centangApr.firstElementChild.classList.replace('fa-times', 'fa-check')
        if ('verifikasi' === d.status) {
            centangApr.classList.replace('btn-success', 'btn-warning')
            centangApr.firstElementChild.classList.replace('fa-check', 'fa-exclamation')
        }
    }
    if ('mei' === d.bulan) {
        centangMei.removeAttribute('href')
        centangMei.classList.replace('btn-danger', 'btn-success')
        centangMei.firstElementChild.classList.replace('fa-times', 'fa-check')
        if ('verifikasi' === d.status) {
            centangMei.classList.replace('btn-success', 'btn-warning')
            centangMei.firstElementChild.classList.replace('fa-check', 'fa-exclamation')
        }
    }
    if ('juni' === d.bulan) {
        centangJun.removeAttribute('href')
        centangJun.classList.replace('btn-danger', 'btn-success')
        centangJun.firstElementChild.classList.replace('fa-times', 'fa-check')
        if ('verifikasi' === d.status) {
            centangJun.classList.replace('btn-success', 'btn-warning')
            centangJun.firstElementChild.classList.replace('fa-check', 'fa-exclamation')
        }
    }
    if ('juli' === d.bulan) {
        centangJul.removeAttribute('href')
        centangJul.classList.replace('btn-danger', 'btn-success')
        centangJul.firstElementChild.classList.replace('fa-times', 'fa-check')
        if ('verifikasi' === d.status) {
            centangJul.classList.replace('btn-success', 'btn-warning')
            centangJul.firstElementChild.classList.replace('fa-check', 'fa-exclamation')
        }
    }
    if ('agustus' === d.bulan) {
        centangAug.removeAttribute('href')
        centangAug.classList.replace('btn-danger', 'btn-success')
        centangAug.firstElementChild.classList.replace('fa-times', 'fa-check')
        if ('verifikasi' === d.status) {
            centangAug.classList.replace('btn-success', 'btn-warning')
            centangAug.firstElementChild.classList.replace('fa-check', 'fa-exclamation')
        }
    }
    if ('september' === d.bulan) {
        centangSep.removeAttribute('href')
        centangSep.classList.replace('btn-danger', 'btn-success')
        centangSep.firstElementChild.classList.replace('fa-times', 'fa-check')
        if ('verifikasi' === d.status) {
            centangSep.classList.replace('btn-success', 'btn-warning')
            centangSep.firstElementChild.classList.replace('fa-check', 'fa-exclamation')
        }
    }
    if ('oktober' === d.bulan) {
        centangOct.removeAttribute('href')
        centangOct.classList.replace('btn-danger', 'btn-success')
        centangOct.firstElementChild.classList.replace('fa-times', 'fa-check')
        if ('verifikasi' === d.status) {
            centangOct.classList.replace('btn-success', 'btn-warning')
            centangOct.firstElementChild.classList.replace('fa-check', 'fa-exclamation')
        }
    }
    if ('november' === d.bulan) {
        centangNov.removeAttribute('href')
        centangNov.classList.replace('btn-danger', 'btn-success')
        centangNov.firstElementChild.classList.replace('fa-times', 'fa-check')
        if ('verifikasi' === d.status) {
            centangNov.classList.replace('btn-success', 'btn-warning')
            centangNov.firstElementChild.classList.replace('fa-check', 'fa-exclamation')
        }
    }
    if ('desember' === d.bulan) {
        centangDes.removeAttribute('href')
        centangDes.classList.replace('btn-danger', 'btn-success')
        centangDes.firstElementChild.classList.replace('fa-times', 'fa-check')
        if ('verifikasi' === d.status) {
            centangDes.classList.replace('btn-success', 'btn-warning')
            centangDes.firstElementChild.classList.replace('fa-check', 'fa-exclamation')
        }
    }
})
const janClaslist = Array.from(centangJan.classList)
const febClaslist = Array.from(centangFeb.classList)
const marClaslist = Array.from(centangMar.classList)
const aprClaslist = Array.from(centangApr.classList)
const meiClaslist = Array.from(centangMei.classList)
const junClaslist = Array.from(centangJun.classList)
const julClaslist = Array.from(centangJul.classList)
const augClaslist = Array.from(centangAug.classList)
const sepClaslist = Array.from(centangSep.classList)
const octClaslist = Array.from(centangOct.classList)
const novClaslist = Array.from(centangNov.classList)
const desClaslist = Array.from(centangDes.classList)

if (janClaslist.includes('btn-danger')) {
    centangJan.removeAttribute('href')
    centangJan.setAttribute('href', `${window.origin}/konfirmasi/iuranbulanan?bulan=januari&tahun=${tahundata.value.replace(/\s+/g, '')}`)
}
if (febClaslist.includes('btn-danger')) {
    centangFeb.removeAttribute('href')
    centangFeb.setAttribute('href', `${window.origin}/konfirmasi/iuranbulanan?bulan=febuari&tahun=${tahundata.value.replace(/\s+/g, '')}`)
}
if (marClaslist.includes('btn-danger')) {
    centangMar.removeAttribute('href')
    centangMar.setAttribute('href', `${window.origin}/konfirmasi/iuranbulanan?bulan=maret&tahun=${tahundata.value.replace(/\s+/g, '')}`)
}
if (aprClaslist.includes('btn-danger')) {
    centangApr.removeAttribute('href')
    centangApr.setAttribute('href', `${window.origin}/konfirmasi/iuranbulanan?bulan=april&tahun=${tahundata.value.replace(/\s+/g, '')}`)
}
if (meiClaslist.includes('btn-danger')) {
    centangMei.removeAttribute('href')
    centangMei.setAttribute('href', `${window.origin}/konfirmasi/iuranbulanan?bulan=mei&tahun=${tahundata.value.replace(/\s+/g, '')}`)
}
if (junClaslist.includes('btn-danger')) {
    centangJun.removeAttribute('href')
    centangJun.setAttribute('href', `${window.origin}/konfirmasi/iuranbulanan?bulan=juni&tahun=${tahundata.value.replace(/\s+/g, '')}`)
}
if (julClaslist.includes('btn-danger')) {
    centangJul.removeAttribute('href')
    centangJul.setAttribute('href', `${window.origin}/konfirmasi/iuranbulanan?bulan=juli&tahun=${tahundata.value.replace(/\s+/g, '')}`)
}
if (augClaslist.includes('btn-danger')) {
    centangAug.removeAttribute('href')
    centangAug.setAttribute('href', `${window.origin}/konfirmasi/iuranbulanan?bulan=agustus&tahun=${tahundata.value.replace(/\s+/g, '')}`)
}
if (sepClaslist.includes('btn-danger')) {
    centangSep.removeAttribute('href')
    centangSep.setAttribute('href', `${window.origin}/konfirmasi/iuranbulanan?bulan=september&tahun=${tahundata.value.replace(/\s+/g, '')}`)
}
if (octClaslist.includes('btn-danger')) {
    centangOct.removeAttribute('href')
    centangOct.setAttribute('href', `${window.origin}/konfirmasi/iuranbulanan?bulan=oktober&tahun=${tahundata.value.replace(/\s+/g, '')}`)
}
if (novClaslist.includes('btn-danger')) {
    centangNov.removeAttribute('href')
    centangNov.setAttribute('href', `${window.origin}/konfirmasi/iuranbulanan?bulan=november&tahun=${tahundata.value.replace(/\s+/g, '')}`)
}
if (desClaslist.includes('btn-danger')) {
    centangDes.removeAttribute('href')
    centangDes.setAttribute('href', `${window.origin}/konfirmasi/iuranbulanan?bulan=desember&tahun=${tahundata.value.replace(/\s+/g, '')}`)
}
