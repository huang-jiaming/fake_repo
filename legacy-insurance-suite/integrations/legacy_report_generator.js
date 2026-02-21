/**
 * Legacy Report Generator - Node.js utility
 * FICTIONAL DEMO - Do not use in production
 * Uses outdated callback style
 */

var fs = require('fs');

function generateReport(data, outputPath, callback) {
  if (!callback) {
    throw new Error('Callback required');
  }
  var csv = 'policy_id,amount,status\n';
  data.forEach(function(row) {
    csv += row.join(',') + '\n';
  });
  fs.writeFile(outputPath, csv, function(err) {
    if (err) return callback(err);
    callback(null, outputPath);
  });
}

module.exports = { generateReport };
