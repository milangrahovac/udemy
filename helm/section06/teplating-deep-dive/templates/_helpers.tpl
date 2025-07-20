{{- define "templating-deep-dive.fullname" -}}
{{- $defaultName := printf "%s-%s" .Release.Name .Chart.Name -}}
{{- .Values.customName | default $defaultName | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "templating-deep-dive.selectorLabels" -}}
app: {{ .Chart.Name }}
release: {{ .Release.Name }}
managed-by: "helm"
{{- end -}}

{{/* Expect port on int */}}
{{- define "templating-deep-dive.validators.portRange" -}}
{{- $sanitizedPort := int . -}}
{{/* Port validation */}}
{{- if or (lt $sanitizedPort 1) (gt $sanitizedPort 65535) -}}
{{- fail "\n\nError: Ports must always be between 1 and 65535." -}}
{{- end -}}
{{- end -}}

{{- define "templating-deep-dive.validators.service" -}}

{{- include "templating-deep-dive.validators.portRange" .port -}}

{{/* Service type validation */}}
{{- $allowedSvcType := list "ClusterIP" "NodePort" -}}
{{- if not (has .type $allowedSvcType) -}}
{{- fail (printf "\n\nError: Invalid service type %s. \nSupported values are: %s" .type (join ", " $allowedSvcType)) -}}
{{- end -}}

{{- end -}}

## {{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}


# {{- define "templating-deep-dive.fullname1" -}}
# {{- $fullName := printf "%s-%s" .Release.Name .Chart.Name -}}

# {{- if .Values.customName }}
# {{- $fullName = .Values.customName }}
# {{- end }}

# {{- $fullName | trunc 63 | trimSuffix "-" -}}
# {{- end -}}