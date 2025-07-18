{{- define "templating-deep-dive.fullname" -}}
{{- $defaultName := printf "%s-%s" .Release.Name .Chart.Name -}}
{{- .Values.customName | default $defaultName | trunc 63 | trimSuffix "-" -}}
{{- end -}}


{{- define "templating-deep-dive.selectorLabels" -}}
app: {{ .Chart.Name }}
release: {{ .Release.Name }}
managed-by: "helm"
{{- end -}}

## {{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}


# {{- define "templating-deep-dive.fullname1" -}}
# {{- $fullName := printf "%s-%s" .Release.Name .Chart.Name -}}

# {{- if .Values.customName }}
# {{- $fullName = .Values.customName }}
# {{- end }}

# {{- $fullName | trunc 63 | trimSuffix "-" -}}
# {{- end -}}