const CryptoJS = require("C:\\Program Files\\nodejs\\node_modules\\crypto-js");
var key = "aaad3e4fd540b0f79dca95606e72bf93"
window = global;

function decryptUrl(ciphertext) {
    return CryptoJS.AES.decrypt(
        {ciphertext: CryptoJS.enc.Base64url.parse(ciphertext)},
        CryptoJS.enc.Hex.parse(key),
        {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7,
        }
    ).toString(CryptoJS.enc.Utf8);
}

function bytesToWords(t) {
    for (var n = [], r = 0, e = 0; r < t.length; r++, e += 8) n[e >>> 5] |= t[r] << 24 - e % 32;
    return n
}


function wordsToBytes(t) {
    for (var n = [], r = 0; r < 32 * t.length; r += 8) n.push(t[r >>> 5] >>> 24 - r % 32 & 255);
    return n
}

function stringToBytes(t) {
    for (var n = [], r = 0; r < t.length; r++) n.push(255 & t.charCodeAt(r));
    return n
}

function bytesToString(t) {
    for (var n = [], r = 0; r < t.length; r++) n.push(String.fromCharCode(t[r]));
    return n.join('')
}



var n = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

rotl = function (t, n) {
    return t << n | t >>> 32 - n
}
rotr = function (t, n) {
    return t << 32 - n | t >>> n
}

endian = function (t) {
    if (t.constructor == Number) return 16711935 & rotl(t, 8) | 4278255360 & rotl(t, 24);
    for (var n = 0; n < t.length; n++) t[n] = endian(t[n]);
    return t
}


function c() {
    var t, n = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {},
        e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : "",
        o = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : {}, i = !1, c = !1, a = "json",
        l = r({}, n), u = s.isInClient();
    "function" == typeof o ? t = o : (t = o.callback,
        i = o.useH5 || !1,
        a = o.postType || "json",
        c = o.isCDN || !1),
    e && ("[object Object]" != Object.prototype.toString.call(e) ? u = !1 : "urlencoded" == a && (u = !1));
    var f = function () {
        var n = (new Date).getTime()
            , i = []
            , s = []
            , u = "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"
            , f = {
            srcappid: "2919",
            clientver: "20000",
            clienttime: n,
            mid: n,
            uuid: n,
            dfid: "-"
        };
        c && (delete f.clienttime,
            delete f.mid,
            delete f.uuid,
            delete f.dfid),
            l = r({}, f, {}, l);
        for (var g in l)
            i.push(g);
        if (i.sort(),
            i.forEach(function (t) {
                s.push(t + "=" + l[t])
            }),
            e)
            if ("[object Object]" == Object.prototype.toString.call(e))
                if ("json" == a)
                    s.push(JSON.stringify(e));
                else {
                    var b = [];
                    for (var g in e)
                        b.push(g + "=" + e[g]);
                    s.push(b.join("&"))
                }
            else
                s.push(e);
        s.unshift(u),
            s.push(u),
            l.signature = d(s.join("")),
        o.log && (console.log("H5签名前参数", s),
            console.log("H5签名后返回", l)),
            e ? t && t(l, "[object Object]" == Object.prototype.toString.call(e) && "json" == a ? JSON.stringify(e) : e) : t && t(l)
    };
    if (u && !i) {
        var g = !1;
        s.mobileCall(764, {
            get: l,
            post: e
        }, function (n) {
            return !g && (g = !0,
                n && n.status ? (delete n.status,
                o.log && (console.log("客户端签名前参数", {
                    get: l,
                    post: e
                }),
                    console.log("客户端签名后返回", r({}, l, {}, n))),
                    l = r({}, l, {}, n),
                    e ? t && t(l, "[object Object]" == Object.prototype.toString.call(e) && "json" == a ? JSON.stringify(e) : e) : t && t(l),
                    !1) : (u = !1,
                    void f()))
        })
    } else
        u = !1,
            f()
}


function r(r) {
    for (var e = 1; e < arguments.length; e++) {
        var o = null != arguments[e] ? arguments[e] : {};
        e % 2 ? n(o, !0).forEach(function (n) {
            t(r, n, o[n])
        }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(r, Object.getOwnPropertyDescriptors(o)) : n(o).forEach(function (t) {
            Object.defineProperty(r, t, Object.getOwnPropertyDescriptor(o, t))
        })
    }
    return r
}

function n(t, n) {
    var r = Object.keys(t);
    if (Object.getOwnPropertySymbols) {
        var e = Object.getOwnPropertySymbols(t);
        n && (e = e.filter(function (n) {
            return Object.getOwnPropertyDescriptor(t, n).enumerable
        })),
            r.push.apply(r, e)
    }
    return r
}


// console.log(bytesToWords([78,86,80,104,53,111,111,55]))
//
// console.log(wordsToBytes([670516747,1218133826,238919402,-483841248]))

t = 'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtappid=1014clienttime=1710575129698clientver=20000dfid=34cfyK0OUOqA2L0DLT4EBTtmencode_album_audio_id=a4ugpa90mid=103cd3fcda7117a575067d21c185b075platid=4srcappid=2919token=userid=0uuid=103cd3fcda7117a575067d21c185b075NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt'
// console.log(decry(t, null))

// t ={dfid: '34cfyK0OUOqA2L0DLT4EBTtm',
//     appid: 1014, mid: '103cd3fcda7117a575067d21c185b075',
//     platid: 4, encode_album_audio_id: '4738mfc3',
// }
_ff = function (t, n, r, e, o, i, c) {
    var s = t + (n & r | ~n & e) + (o >>> 0) + c;
    return (s << i | s >>> 32 - i) + n
}

_gg = function (t, n, r, e, o, i, c) {
    var s = t + (n & e | r & ~e) + (o >>> 0) + c;
    return (s << i | s >>> 32 - i) + n
}

_hh = function (t, n, r, e, o, i, c) {
    var s = t + (n ^ r ^ e) + (o >>> 0) + c;
    return (s << i | s >>> 32 - i) + n
}

_ii = function (t, n, r, e, o, i, c) {
    var s = t + (r ^ (n | ~e)) + (o >>> 0) + c;
    return (s << i | s >>> 32 - i) + n
}

endian = function (t) {
    if (t.constructor == Number)
        return 16711935 & rotl(t, 8) | 4278255360 & rotl(t, 24);
    for (var n = 0; n < t.length; n++)
        t[n] = endian(t[n]);
    return t
}

bytesToHex = function (t) {
    for (var n = [], r = 0; r < t.length; r++)
        n.push((t[r] >>> 4).toString(16)),
            n.push((15 & t[r]).toString(16));
    return n.join("")
}

i = function (t, c) {
    t.constructor == String ? t = c && "binary" === c.encoding ? stringToBytes(t) : stringToBytes(t) : e(t) ? t = Array.prototype.slice.call(t, 0) : Array.isArray(t) || (t = t.toString());
    for (var s = bytesToWords(t), a = 8 * t.length, l = 1732584193, u = -271733879, f = -1732584194, d = 271733878, g = 0; g < s.length; g++)
        s[g] = 16711935 & (s[g] << 8 | s[g] >>> 24) | 4278255360 & (s[g] << 24 | s[g] >>> 8);
    s[a >>> 5] |= 128 << a % 32,
        s[14 + (a + 64 >>> 9 << 4)] = a;
    for (var b = _ff, p = _gg, h = _hh, m = _ii, g = 0; g < s.length; g += 16) {
        var y = l
            , j = u
            , S = f
            , v = d;
        u = m(u = m(u = m(u = m(u = h(u = h(u = h(u = h(u = p(u = p(u = p(u = p(u = b(u = b(u = b(u = b(u, f = b(f, d = b(d, l = b(l, u, f, d, s[g + 0], 7, -680876936), u, f, s[g + 1], 12, -389564586), l, u, s[g + 2], 17, 606105819), d, l, s[g + 3], 22, -1044525330), f = b(f, d = b(d, l = b(l, u, f, d, s[g + 4], 7, -176418897), u, f, s[g + 5], 12, 1200080426), l, u, s[g + 6], 17, -1473231341), d, l, s[g + 7], 22, -45705983), f = b(f, d = b(d, l = b(l, u, f, d, s[g + 8], 7, 1770035416), u, f, s[g + 9], 12, -1958414417), l, u, s[g + 10], 17, -42063), d, l, s[g + 11], 22, -1990404162), f = b(f, d = b(d, l = b(l, u, f, d, s[g + 12], 7, 1804603682), u, f, s[g + 13], 12, -40341101), l, u, s[g + 14], 17, -1502002290), d, l, s[g + 15], 22, 1236535329), f = p(f, d = p(d, l = p(l, u, f, d, s[g + 1], 5, -165796510), u, f, s[g + 6], 9, -1069501632), l, u, s[g + 11], 14, 643717713), d, l, s[g + 0], 20, -373897302), f = p(f, d = p(d, l = p(l, u, f, d, s[g + 5], 5, -701558691), u, f, s[g + 10], 9, 38016083), l, u, s[g + 15], 14, -660478335), d, l, s[g + 4], 20, -405537848), f = p(f, d = p(d, l = p(l, u, f, d, s[g + 9], 5, 568446438), u, f, s[g + 14], 9, -1019803690), l, u, s[g + 3], 14, -187363961), d, l, s[g + 8], 20, 1163531501), f = p(f, d = p(d, l = p(l, u, f, d, s[g + 13], 5, -1444681467), u, f, s[g + 2], 9, -51403784), l, u, s[g + 7], 14, 1735328473), d, l, s[g + 12], 20, -1926607734), f = h(f, d = h(d, l = h(l, u, f, d, s[g + 5], 4, -378558), u, f, s[g + 8], 11, -2022574463), l, u, s[g + 11], 16, 1839030562), d, l, s[g + 14], 23, -35309556), f = h(f, d = h(d, l = h(l, u, f, d, s[g + 1], 4, -1530992060), u, f, s[g + 4], 11, 1272893353), l, u, s[g + 7], 16, -155497632), d, l, s[g + 10], 23, -1094730640), f = h(f, d = h(d, l = h(l, u, f, d, s[g + 13], 4, 681279174), u, f, s[g + 0], 11, -358537222), l, u, s[g + 3], 16, -722521979), d, l, s[g + 6], 23, 76029189), f = h(f, d = h(d, l = h(l, u, f, d, s[g + 9], 4, -640364487), u, f, s[g + 12], 11, -421815835), l, u, s[g + 15], 16, 530742520), d, l, s[g + 2], 23, -995338651), f = m(f, d = m(d, l = m(l, u, f, d, s[g + 0], 6, -198630844), u, f, s[g + 7], 10, 1126891415), l, u, s[g + 14], 15, -1416354905), d, l, s[g + 5], 21, -57434055), f = m(f, d = m(d, l = m(l, u, f, d, s[g + 12], 6, 1700485571), u, f, s[g + 3], 10, -1894986606), l, u, s[g + 10], 15, -1051523), d, l, s[g + 1], 21, -2054922799), f = m(f, d = m(d, l = m(l, u, f, d, s[g + 8], 6, 1873313359), u, f, s[g + 15], 10, -30611744), l, u, s[g + 6], 15, -1560198380), d, l, s[g + 13], 21, 1309151649), f = m(f, d = m(d, l = m(l, u, f, d, s[g + 4], 6, -145523070), u, f, s[g + 11], 10, -1120210379), l, u, s[g + 2], 15, 718787259), d, l, s[g + 9], 21, -343485551),
            l = l + y >>> 0,
            u = u + j >>> 0,
            f = f + S >>> 0,
            d = d + v >>> 0
    }
    return endian([l, u, f, d])
};

function exports(t, r) {
    if (void 0 === t || null === t)
        throw new Error("Illegal argument " + t);
    var e = wordsToBytes(i(t, r));
    return r && r.asBytes ? e : r && r.asString ? bytesToString(e) : bytesToHex(e)
}


// t=[32711812, 685611487, -1088092953, 844736235]
//
//  console.log(wordsToBytes(t))

e = [1, 243, 36, 132, 40, 221, 153, 223, 191, 37, 4, 231, 50, 89, 166, 235]

console.log(exports(t))

// t1=[4086879045, 3131620135, 1111335966, 2429183599]

// console.log(endian(t1))

// console.log(i)

