// decrypt.js

// 引入 pako 和 crypto-js
const pako = require('pako');
const crypto = require('crypto-js');

// 定义解压缩函数 inflateAndDecode
function inflateAndDecode(data) {
    let outputString = "";
    const decompressedData = pako.inflate(new Uint8Array(data.match(/[\da-f]{2}/gi).map(function(byte) {
        return parseInt(byte, 16);
    })));

    const chunkSize = 16384;
    for (let i = 0; i < decompressedData.length / chunkSize; i++) {
        outputString += String.fromCharCode.apply(null, decompressedData.slice(i * chunkSize, (i + 1) * chunkSize));
    }

    outputString += String.fromCharCode.apply(null, decompressedData.slice((decompressedData.length / chunkSize) * chunkSize));
    return decodeURIComponent(escape(outputString));
}

// 定义解密函数 decryptAndDecompress
function decryptAndDecompress(encryptedData) {
    try {
        console.log("Encrypted Data:", encryptedData);

        // 使用 AES 解密
        const decryptedHex = crypto.AES.decrypt(encryptedData, crypto.enc.Utf8.parse("c2814b00331f4bf9"), {
            mode: crypto.mode.ECB,
            padding: crypto.pad.Pkcs7
        }).toString(crypto.enc.Hex);

        console.log("Decrypted Hex:", decryptedHex);

        if (!decryptedHex) {
            console.error("Decryption failed or returned empty.");
            return null;
        }

        // 调用 inflateAndDecode 进行解压缩
        const result = inflateAndDecode(decryptedHex);
        console.log("Final Result:", result);

        return result; // 返回解密并解压缩后的结果
    } catch (error) {
        console.error("Error during decryption:", error);
        return null;
    }
}

// 导出 decryptAndDecompress 函数
module.exports = decryptAndDecompress;
